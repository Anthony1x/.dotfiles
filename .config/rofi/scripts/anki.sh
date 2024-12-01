#!/bin/bash

script_dir="$HOME/Documents/Dev/vn-cards"

# List of scripts
scripts=(
    "Screenshot and append to latest card:$script_dir/take_screenshot.sh"
    "Screenshot and start/stop recording:$script_dir/record_audio.sh"
    "Start tag latest card:$script_dir/tag_card.php --start"
    "Stop tag latest card:$script_dir/tag_card.php --stop"
    "Fill fields from tags:$script_dir/copy_from_previous.php"
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
