#!/bin/bash

# Get the connected monitor name (assuming only DP-4 is relevant)
monitor=$(xrandr --query | grep "connected" | grep -Eo '[^ ]+$' | head -n 1)

xrandr --delmonitor virtual1
xrandr --delmonitor virtual2
xrandr --delmonitor virtual3

xrandr --fb 5121x1440
xrandr --fb 5120x1440
