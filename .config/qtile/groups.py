from keys import keys, mod, shift, terminal
from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy

# Create labels for groups and assign them a default layout.
groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#group_labels = ["󰖟", "", "", "", "", "", "", "", "ﭮ", "", "", "﨣", "F1", "F2", "F3", "F4", "F5"]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(), desc="Mod + number to move to that group."),
        Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group."),
        Key([mod, shift], "Tab", lazy.screen.prev_group(), desc="Move to previous group."),
        Key([mod, shift], i.name, lazy.window.togroup(i.name), desc="Move focused window to new group."),
    ])

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", f"{terminal} --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown("top", f"{terminal} --class=scratch -e btop", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", f"{terminal} --class=volume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))
