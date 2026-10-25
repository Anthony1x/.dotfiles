from libqtile.config import Group, ScratchPad, DropDown, Key
from libqtile.lazy import lazy
from settings import terminal, mod, shift, super_disabled

groups: list[Group | ScratchPad] = []
group_keys: list[Key] = []

group_specs: list[tuple[str, str, str]] = [
    ("circumflex", "dead_circumflex", "^"),
    ("1", "1", "1"),
    ("2", "2", "2"),
    ("3", "3", "3"),
    ("4", "4", "4"),
    ("5", "5", "5"),
    ("6", "6", "6"),
    ("7", "7", "7"),
    ("8", "8", "8"),
    ("9", "9", "9"),
    ("0", "0", "0"),
    ("ssharp", "ssharp", "ß"),
    ("dead_acute", "dead_acute", "´"),
]

group_names = [name for name, _, _ in group_specs]
group_labels = [label for _, _, label in group_specs]

for group_name, key_name, label in group_specs:
    groups.append(
        Group(
            name=group_name,
            layout='monadtall',
            label=label,
        ))
    
    group_keys.extend([
        Key([mod], key_name, lazy.group[group_name].toscreen(),
            desc=f"Switch to group {label}"),
        Key([mod, shift], key_name, lazy.window.togroup(group_name),
            desc=f"Move focused window to group {label}"),
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
if not super_disabled:
    group_keys.extend([
        Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('term')),
        Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
        Key([mod, shift], "n", lazy.group['scratchpad'].dropdown_toggle('top')),
    ])
