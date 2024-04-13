from colors import colors
from libqtile import layout
from libqtile.config import Match

# Define layouts and layout themes
layout_theme = {
        "margin":6,
        "border_width": 2,
        "border_focus": colors[7],
        "border_normal": colors[2]
    }

layouts = [
  layout.MonadTall(**layout_theme)
  # layout.MonadWide(**layout_theme),
  # layout.MonadThreeCol(**layout_theme),
  # layout.Floating(**layout_theme),
  # layout.Spiral(**layout_theme),
  # layout.RatioTile(**layout_theme),
  # layout.Max(**layout_theme)
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)