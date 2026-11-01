"""Custom bar widgets."""

import asyncio

import pulsectl_asyncio
from pulsectl import PulseError

from libqtile.utils import create_task
from libqtile.widget import base


class PulseMicVolume(base._TextBox):
    """Volume of the default input (microphone), event driven.

    qtile's Volume widget polls `amixer` every 0.2s through a shell. On Wayland
    qtile is also the compositor, so those forks block frame rendering and
    cause constant stutter in games. This one holds a single PulseAudio/PipeWire
    connection and only updates when the server reports a change. Output format
    matches the Volume widget ("42%" / "M") so the same `fmt` works.
    """

    defaults = [
        ("unmute_format", "{volume}%", "Format when not muted"),
        ("mute_format", "M", "Format when muted"),
    ]

    def __init__(self, **config):
        base._TextBox.__init__(self, "", **config)
        self.add_defaults(PulseMicVolume.defaults)
        self._task = None

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        self._task = create_task(self._listen())

    async def _listen(self):
        while True:
            try:
                async with pulsectl_asyncio.PulseAsync("qtile-mic-volume") as pulse:
                    await self._refresh(pulse)
                    async for _ in pulse.subscribe_events("source", "server"):
                        await self._refresh(pulse)
            except (PulseError, OSError):
                pass
            self.update(self.mute_format)  # server went away, retry shortly
            await asyncio.sleep(5)

    async def _refresh(self, pulse):
        info = await pulse.server_info()
        sources = [s for s in await pulse.source_list() if s.name == info.default_source_name]
        if not sources:
            self.update(self.mute_format)
        elif sources[0].mute:
            self.update(self.mute_format)
        else:
            self.update(self.unmute_format.format(volume=round(sources[0].volume.value_flat * 100)))

    def finalize(self):
        if self._task:
            self._task.cancel()
        base._TextBox.finalize(self)


def speed_up_bar():
    """Cut the cost of a bar redraw (measured: ~72ms -> see commit message).

    On Wayland qtile is the compositor and runs on one thread, so a 70ms bar
    redraw freezes every window (visible as mouse/game hitches, twice a second).
    Profiling showed two things redone from scratch on every redraw although
    their inputs never change:

    1. StatusNotifier: Img.resize() assigns width/height, and qtile's descriptor
       resets the cached surface on *every* assignment, even with an unchanged
       value, so each tray icon is decoded from its PNG on every redraw.
    2. GroupBox: box_width() measures the text of all groups with pango each time.
    3. Some tray apps still invalidate their icon on every redraw, so decoded
       image files are cached per (bytes, size). qtile finish()es surfaces on
       reset, so every caller gets its own cheap copy of the decoded master.
    """
    import cairocffi
    from libqtile import images
    from libqtile.widget.groupbox import _GroupBase

    # config.py runs again on every reload but the process (and so the patched
    # classes) stays, hence one guard per patch.

    if not getattr(images._Resetter, "_dots_patched", False):
        missing = object()
        orig_set = images._Resetter.__set__

        def set_if_changed(self, obj, value):
            if getattr(obj, self.under_name, missing) == value:
                return
            orig_set(self, obj, value)

        images._Resetter.__set__ = set_if_changed
        images._Resetter._dots_patched = True

    if not getattr(_GroupBase, "_dots_patched", False):
        orig_box_width = _GroupBase.box_width
        widths = {}

        def box_width(self, groups):
            key = (
                id(self), tuple(g.label for g in groups), self.font, self.fontsize,
                self.markup, self.padding_x, self.borderwidth,
            )
            try:
                return widths[key]
            except KeyError:
                return widths.setdefault(key, orig_box_width(self, groups))

        _GroupBase.box_width = box_width
        _GroupBase._dots_patched = True

    if not getattr(images.ImageFileBackend, "_dots_patched", False):
        orig_get_surface = images.ImageFileBackend.get_surface
        decoded = {}

        def get_surface(self, width=None, height=None):
            key = (self.bytes_img, width, height)
            master = decoded.get(key)
            if master is None:
                master = orig_get_surface(self, width, height)
                if len(decoded) > 64:
                    decoded.clear()
                decoded[key] = master
            copy = cairocffi.ImageSurface(
                master.get_format(), master.get_width(), master.get_height())
            with cairocffi.Context(copy) as ctx:
                ctx.set_operator(cairocffi.OPERATOR_SOURCE)
                ctx.set_source_surface(master)
                ctx.paint()
            return copy

        images.ImageFileBackend.get_surface = get_surface
        images.ImageFileBackend._dots_patched = True
