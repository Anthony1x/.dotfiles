from colors import colors
from libqtile import layout
from libqtile.config import Match
from variables import layout_theme, layout_theme_floating

layouts = [
  layout.MonadTall(**layout_theme),
  layout.MonadWide(**layout_theme),
]

floating_layout = layout.Floating(
    **layout_theme_floating,
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
