#!/bin/bash

script_dir="$HOME/Documents/Dev/vn-cards"

# List of scripts
scripts=(
    "Screenshot and append to latest card:$script_dir/capture.sh"
    "Screenshot and start/stop recording:$script_dir/capture.sh --record"
)

# Show the menu with rofi
chosen=$(printf "%s\n" "${scripts[@]}" | rofi -dmenu -p "Select Anki action")

# Execute the chosen script
if [ -n "$chosen" ]; then
    # Extract the script path (the part after the colon)
    script_path=$(echo "$chosen" | cut -d':' -f2)

    # Extract the script name without options
    script_name=$(echo "$script_path" | cut -d' ' -f1)

    # Extract options (if any)
    options=$(echo "$script_path" | cut -d' ' -f2-)

    # Check the file extension and execute accordingly
    if [[ "$script_name" == *.sh ]]; then
        bash "$script_path"
    elif [[ "$script_name" == *.php ]]; then
        php "$script_name" $options # Pass the options separately
    else
        dunstify "Unsupported script type."
    fi
fi
