#!/bin/bash

# Define the layouts
layouts=(
    "16:9 middle"
    "18:9 middle"
    "4:3 middle"
    "21:9 + 11:9"
    "11:9 + 21:9"
    "21:9 middle"
    "2x 16:9 side by side"
    "32:9, no fake screens"
)

# Display the layouts in Rofi and get the selected index
selected=$(printf "%s\n" "${layouts[@]}" | rofi -dmenu -p "Select Screen Layout:")

# Check if a selection was made
if [ -n "$selected" ]; then
    # Get the index of the selected layout
    index=$(printf "%s\n" "${layouts[@]}" | grep -n "^$selected$" | cut -d: -f1)

    python3 ~/.config/rofi/scripts/update.py $index

    qtile cmd-obj -o cmd -f reload_config
fi
