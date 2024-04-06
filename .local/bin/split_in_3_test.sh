#!/bin/bash

# Get the connected monitor name (assuming only DP-4 is relevant)
monitor=$(xrandr --query | grep "connected" | grep -Eo '[^ ]+$' | head -n 1)

# Create the virtual monitors using xrandr commands
xrandr --setmonitor virtual1 "1280/1x1440/1+0+0" none
xrandr --setmonitor virtual2 "2560/1x1440/1+1280+0" DP-4
xrandr --setmonitor virtual3 "1280/1x1440/1+3840+0" none

xrandr --fb 5121x1440
xrandr --fb 5120x1440

echo "Virtual monitors created successfully!"
