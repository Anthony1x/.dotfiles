#!/bin/sh
# One-time (idempotent) setup for running Qtile on Wayland.
#   - links the portal configs into ~/.config
# Packages are listed in the README.
set -e
here=$(cd "$(dirname "$0")" && pwd)

mkdir -p ~/.config/xdg-desktop-portal ~/.config/xdg-desktop-portal-wlr
ln -sf "$here/qtile-portals.conf" ~/.config/xdg-desktop-portal/qtile-portals.conf
ln -sf "$here/xdg-desktop-portal-wlr.conf" ~/.config/xdg-desktop-portal-wlr/config
echo "Done."
