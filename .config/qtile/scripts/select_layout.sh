#!/bin/bash

# Fetch layouts from python config
# We need to add the directory to python path so it can import fake_screens
layouts_list=$(python3 -c "import sys; sys.path.append('/home/anthony/dotfiles/.config/qtile'); from fake_screens import layout_config; print('\n'.join([l['name'] for l in layout_config]))")

# Display the layouts in Rofi and get the selected index
selected=$(echo "$layouts_list" | rofi -dmenu -p "Select Screen Layout:")

# Check if a selection was made
if [ -n "$selected" ]; then
    # Get the index of the selected layout
    index=$(echo "$layouts_list" | grep -n "^$selected$" | cut -d: -f1)

    python3 ~/.config/qtile/scripts/update.py $index

    qtile cmd-obj -o cmd -f reload_config
fi