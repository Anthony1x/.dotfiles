# Le my dots

Necessary programs to run on

```
sudo pacman -S qtile qtile-extras kitty picom ttf-jetbrains-mono ttf-jetbrains-mono-nerd thunar btop dunst redshift feh
```


## Wayland

Qtile also runs on Wayland (pick the Wayland qtile entry in the display manager). The same
config is used for both backends; `settings.is_wayland` switches the differences.

Fedora:

```
sudo dnf install qtile-wayland grim slurp satty swaylock swayidle gammastep gammastep-indicator \
    swaybg wlr-randr wlopm ydotool xdg-desktop-portal-wlr xdg-desktop-portal-gtk wl-clipboard
.config/qtile/wayland/install.sh   # links the portal configs (screen sharing)
```

Differences from X11: grim instead of scrot/maim, swaylock instead of betterlockscreen,
swaybg instead of feh, gammastep instead of redshift, ydotool instead of xdotool, no picom.
Region screenshot is a key chord (Mod+Alt+S, then W/A/S/D) instead of a keyboard grab.
Session environment variables are set in `config.py`.
