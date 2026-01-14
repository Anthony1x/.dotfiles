from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from settings import terminal, mod, shift

groups: list[Group | ScratchPad] = []
group_keys: list[Key] = []

group_names: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# Add group names, labels, and default layouts to the groups object.
for i in range(len(group_names)):
    name = group_names[i]
    label = group_labels[i]
    
    groups.append(
        Group(
            name=name,
            layout='monadtall',
            label=label,
        ))
    
    group_keys.extend([
        Key([mod], name, lazy.group[name].toscreen(),
            desc=f"Switch to group {name}"),
        Key([mod, shift], name, lazy.window.togroup(name),
            desc=f"Move focused window to group {name}"),
    ])

# Cycle groups
group_keys.extend([
    Key([mod], "Tab", lazy.screen.next_group(), desc="Move to next group."),
    Key([mod, shift], "Tab", lazy.screen.prev_group(),
        desc="Move to previous group."),
])

# Define scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", f"{terminal} --class=scratch",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("top", f"{terminal} --class=scratch -e btop",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", f"{terminal} --class=volume -e pulsemixer",
             width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))

# Scratchpad keybindings
group_keys.extend([
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key([mod, shift], "n", lazy.group['scratchpad'].dropdown_toggle('top')),
])