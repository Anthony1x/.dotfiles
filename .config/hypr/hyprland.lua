--[[
===============================================================================
  hyprland.lua — Ported from qtile config (Catppuccin Mocha / Mauve)
  Fedora 44 | Hyprland 0.55 | Lua config syntax
  ~/.config/hypr/hyprland.lua
===============================================================================
]]

--  ── Colors (ported from colors.py: CATPPUCCIN_MOCHA) ─────────────────────
--  NOTE: Hyprland Lua accepts rgb(XXXXXX), rgba(XXXXXXXX), and 0xXXXXXXXX

local colors = {
	rosewater = "rgb(F5E0DC)",
	flamingo = "rgb(F2CDCD)",
	pink = "rgb(F5C2E7)",
	mauve = "rgb(CBA6F7)",
	red = "rgb(F38BA8)",
	maroon = "rgb(EBA0AC)",
	peach = "rgb(FAB387)",
	yellow = "rgb(F9E2AF)",
	green = "rgb(A6E3A1)",
	teal = "rgb(94E2D5)",
	sky = "rgb(89DCEB)",
	sapphire = "rgb(74C7EC)",
	blue = "rgb(89B4FA)",
	lavender = "rgb(B4BEFE)",
	text = "rgb(CDD6F4)",
	subtext1 = "rgb(BAC2DE)",
	subtext0 = "rgb(A6ADC8)",
	overlay2 = "rgb(9399B2)",
	overlay1 = "rgb(7F849C)",
	surface2 = "rgb(585B70)",
	surface1 = "rgb(45475A)",
	surface0 = "rgb(313244)",
	base = "rgb(1E1E2E)",
	mantle = "rgb(181825)",
	crust = "rgb(11111B)",

	accent = "rgb(CBA6F7)",
	disabled = "rgb(313244)",
	highlight = "rgb(F38BA8)",
}

--  ── Variables (ported from settings.py) ─────────────────────────────────

local mod = "SUPER"
local alt = "ALT"
local shift = "SHIFT"
local control = "CTRL"

local terminal = "kitty"
local menu = "rofi -show drun"
local browser = "floorp"
local files = "thunar"
local screenshot = "env QT_AUTO_SCREEN_SCALE_FACTOR=0 QT_SCREEN_SCALE_FACTORS=1 flameshot gui"
local lock = "loginctl lock-session"
local powermenu =
	"rofi -show power-menu -modi 'power-menu:/home/anthony/dotfiles/.config/rofi/scripts//rofi-power-menu'"

local scripts_dir = os.getenv("HOME") .. "/.config/hypr/scripts"

--  ── Environment Variables (ported from config.py wl_input_rules + autostart) ──

hl.env("XCURSOR_SIZE", "24")
hl.env("XCURSOR_THEME", "catppuccin-mocha-dark-cursors")
hl.env("QT_QPA_PLATFORMTHEME", "qt6ct")

-- NVIDIA (RTX 2080)
hl.env("LIBVA_DRIVER_NAME", "nvidia")
hl.env("__GLX_VENDOR_LIBRARY_NAME", "nvidia")
hl.env("NVD_BACKEND", "direct")

--  ── Monitor Setup (ported from autostart.sh wlr-randr commands) ──────────
--  DP-4: 49" ultrawide 5120x1440@240Hz (main, below the 32")
--  DP-2: 32" 2560x1440@144Hz (secondary, centered above)
--  Run `hyprctl monitors` and adjust if names differ

hl.monitor({
	output = "DP-4",
	mode = "5120x1440@240",
	position = "0x1440",
	scale = 1,
})
hl.monitor({
	output = "DP-2",
	mode = "2560x1440@144",
	position = "1280x0",
	scale = 1,
})

-- Laptop mode (uncomment and comment the above):
-- hl.monitor({ output = "", mode = "preferred", position = "auto", scale = "auto" })

--  ── Autostart (ported from autostart.sh) ─────────────────────────────────

hl.on("hyprland.start", function()
	hl.exec_cmd("waybar")
	hl.exec_cmd("swaybg -i " .. os.getenv("HOME") .. "/Pictures/Wallpaper/Desktop/city.jpg")
	hl.exec_cmd("dunst")
	hl.exec_cmd("fcitx5 -d")
	hl.exec_cmd("/usr/libexec/xdg-desktop-portal")
	hl.exec_cmd("gammastep-indicator -c " .. os.getenv("HOME") .. "/.config/gammastep/gammastep.conf")
	hl.exec_cmd(os.getenv("HOME") .. "/Documents/Dev/vn-cards/scripts/audio-replay-recorder.sh")
end)

--  ── General (ported from config.py flags + settings.py layout_theme) ─────

hl.config({
	general = {
		gaps_in = 6,
		gaps_out = 6,
		border_size = 2,

		col = {
			active_border = colors.accent,
			inactive_border = colors.disabled,
		},

		allow_tearing = false,
		resize_on_border = false,
		layout = "master",
	},

	--  ── Decoration ──────────────────────────────────────────────────────

	decoration = {
		rounding = 10,
		rounding_power = 2,
		dim_inactive = false,
		dim_strength = 0.1,

		blur = {
			enabled = false,
		},

		active_opacity = 1.0,
		inactive_opacity = 1.0,
	},

	--  ── Master Layout (MonadTall equivalent) ─────────────────────────────

	master = {
		orientation = "left",
		mfact = 0.55,
		new_status = "slave",
	},

	--  ── Input (ported from settings.py + wayland InputConfig) ────────────

	input = {
		kb_layout = "de",
		follow_mouse = 1,
		accel_profile = "flat",

		touchpad = {
			natural_scroll = false,
		},
	},

	--  ── Misc (ported from config.py flags) ───────────────────────────────

	misc = {
		disable_hyprland_logo = true,
		disable_splash_rendering = true,
		focus_on_activate = true,
		allow_session_lock_restore = true,
	},
})

--  ── Animation Curves ────────────────────────────────────────────────────

hl.curve("easeOutQuint", { type = "bezier", points = { { 0.23, 1 }, { 0.32, 1 } } })
hl.curve("easeInOutCubic", { type = "bezier", points = { { 0.65, 0.05 }, { 0.36, 1 } } })
hl.curve("linear", { type = "bezier", points = { { 0, 0 }, { 1, 1 } } })
hl.curve("almostLinear", { type = "bezier", points = { { 0.5, 0.5 }, { 0.75, 1 } } })
hl.curve("quick", { type = "bezier", points = { { 0.15, 0 }, { 0.1, 1 } } })
hl.curve("easy", { type = "spring", mass = 1, stiffness = 71.2633, dampening = 15.8273644 })

hl.animation({ leaf = "global", enabled = true, speed = 10, bezier = "default" })
hl.animation({ leaf = "border", enabled = true, speed = 5.39, bezier = "easeOutQuint" })
hl.animation({ leaf = "windows", enabled = true, speed = 4.79, spring = "easy" })
hl.animation({ leaf = "windowsIn", enabled = true, speed = 4.1, spring = "easy", style = "popin 87%" })
hl.animation({ leaf = "windowsOut", enabled = true, speed = 1.49, bezier = "linear", style = "popin 87%" })
hl.animation({ leaf = "fadeIn", enabled = true, speed = 1.73, bezier = "almostLinear" })
hl.animation({ leaf = "fadeOut", enabled = true, speed = 1.46, bezier = "almostLinear" })
hl.animation({ leaf = "fade", enabled = true, speed = 3.03, bezier = "quick" })
hl.animation({ leaf = "layers", enabled = true, speed = 3.81, bezier = "easeOutQuint" })
hl.animation({ leaf = "layersIn", enabled = true, speed = 4, bezier = "easeOutQuint", style = "fade" })
hl.animation({ leaf = "layersOut", enabled = true, speed = 1.5, bezier = "linear", style = "fade" })
hl.animation({ leaf = "fadeLayersIn", enabled = true, speed = 1.79, bezier = "almostLinear" })
hl.animation({ leaf = "fadeLayersOut", enabled = true, speed = 1.39, bezier = "almostLinear" })
hl.animation({ leaf = "workspaces", enabled = true, speed = 1.94, bezier = "almostLinear", style = "fade" })
hl.animation({ leaf = "workspacesIn", enabled = true, speed = 1.21, bezier = "almostLinear", style = "fade" })
hl.animation({ leaf = "workspacesOut", enabled = true, speed = 1.94, bezier = "almostLinear", style = "fade" })
hl.animation({ leaf = "zoomFactor", enabled = true, speed = 7, bezier = "quick" })

--  ── Keybindings (ported from keys.py, groups.py, screens.py) ─────────────

-- Essentials (always active in qtile)
hl.bind(mod .. " + Return", hl.dsp.exec_cmd(terminal))
hl.bind(mod .. " + R", hl.dsp.exec_cmd("rofi -show run"))
hl.bind(mod .. " + " .. shift .. " + Return", hl.dsp.exec_cmd(files))

-- Focus navigation
hl.bind(mod .. " + left", hl.dsp.focus({ direction = "left" }))
hl.bind(mod .. " + right", hl.dsp.focus({ direction = "right" }))
hl.bind(mod .. " + down", hl.dsp.focus({ direction = "down" }))
hl.bind(mod .. " + up", hl.dsp.focus({ direction = "up" }))

-- hl.dsp.focus() only accepts left/right/up/down (no "next")
-- Focus next window: use hl.dsp.focus_cycle("next") if available in your Hyprland version
-- or skip — directional focus keys (arrows) cover this use case

-- Swap windows
hl.bind(mod .. " + " .. shift .. " + left", hl.dsp.window.swap({ direction = "left" }))
hl.bind(mod .. " + " .. shift .. " + right", hl.dsp.window.swap({ direction = "right" }))
hl.bind(mod .. " + " .. shift .. " + down", hl.dsp.window.swap({ direction = "down" }))
hl.bind(mod .. " + " .. shift .. " + up", hl.dsp.window.swap({ direction = "up" }))

-- Focus monitor
hl.bind(mod .. " + " .. control .. " + left", hl.dsp.focus({ monitor = "left" }))
hl.bind(mod .. " + " .. control .. " + right", hl.dsp.focus({ monitor = "right" }))
hl.bind(mod .. " + comma", hl.dsp.focus({ monitor = "left" }))
hl.bind(mod .. " + period", hl.dsp.focus({ monitor = "right" }))

-- Workspaces (1-0, ported from group_names)
for i = 1, 10 do
	local key = i % 10 -- 10 maps to key 0
	hl.bind(mod .. " + " .. key, hl.dsp.focus({ workspace = i }))
	hl.bind(mod .. " + " .. shift .. " + " .. key, hl.dsp.window.move({ workspace = i }))
end

-- Cycle workspaces / groups
hl.bind(mod .. " + Tab", hl.dsp.focus({ workspace = "e+1" }))
hl.bind(mod .. " + " .. shift .. " + Tab", hl.dsp.focus({ workspace = "e-1" }))

-- Layout switching (ported from Alt+Tab cycling MonadTall/MonadWide)
-- In hyprland, cycling layouts = master <-> dwindle <-> scrolling, etc.
hl.bind(alt .. " + Tab", hl.dsp.layout("cyclenext"))
hl.bind(alt .. " + " .. shift .. " + Tab", hl.dsp.layout("cycleprev"))

-- Toggle master orientation (MonadTall <-> MonadWide)
hl.bind(mod .. " + " .. alt .. " + Space", hl.dsp.layout("orientationnext"))

-- Window management (ported from super_disabled block in keys.py)
hl.bind(mod .. " + W", hl.dsp.window.close())
hl.bind(mod .. " + F", hl.dsp.window.fullscreen())
hl.bind(mod .. " + " .. alt .. " + F", hl.dsp.exec_cmd("hyprctl dispatch fakefullscreen"))
hl.bind(mod .. " + " .. shift .. " + F", hl.dsp.window.float({ action = "toggle" }))

hl.bind(mod .. " + D", hl.dsp.exec_cmd(menu))
hl.bind(mod .. " + Q", hl.dsp.exec_cmd(browser))
hl.bind(mod .. " + " .. alt .. " + S", hl.dsp.exec_cmd(screenshot))
hl.bind(mod .. " + " .. alt .. " + L", hl.dsp.exec_cmd(lock))
hl.bind(mod .. " + " .. shift .. " + X", hl.dsp.exec_cmd(powermenu))

-- Resize (ported from shrink/grow)
hl.bind(mod .. " + " .. control .. " + I", hl.dsp.exec_cmd("hyprctl dispatch resizeactive -30 0"))
hl.bind(mod .. " + " .. control .. " + O", hl.dsp.exec_cmd("hyprctl dispatch resizeactive 30 0"))

-- Anki recording scripts
hl.bind(mod .. " + M", hl.dsp.exec_cmd("/home/anthony/Documents/Dev/vn-cards/scripts/capture.sh"))
hl.bind(
	mod .. " + " .. shift .. " + M",
	hl.dsp.exec_cmd("/home/anthony/Documents/Dev/vn-cards/scripts/capture.sh --record")
)
hl.bind(
	mod .. " + " .. control .. " + M",
	hl.dsp.exec_cmd("/home/anthony/Documents/Dev/vn-cards/scripts/audio-replay-save.sh")
)

-- Scratchpads (ported from ScratchPad/DropDown in groups.py)
hl.bind(mod .. " + N", hl.dsp.workspace.toggle_special("term"))
hl.bind(mod .. " + V", hl.dsp.workspace.toggle_special("volume"))
hl.bind(mod .. " + " .. shift .. " + N", hl.dsp.workspace.toggle_special("btop"))

-- Helper: stash current window into scratchpad
hl.bind(mod .. " + " .. control .. " + " .. shift .. " + N", hl.dsp.window.move({ workspace = "special:btop" }))
hl.bind(mod .. " + " .. control .. " + " .. shift .. " + V", hl.dsp.window.move({ workspace = "special:volume" }))

-- Media keys (ported from keys.py - always active, with locked + repeating)
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd(scripts_dir .. "/volume.sh up"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd(scripts_dir .. "/volume.sh down"), { locked = true, repeating = true })
hl.bind("XF86AudioMute", hl.dsp.exec_cmd(scripts_dir .. "/volume.sh mute"), { locked = true, repeating = true })
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"), { locked = true })
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"), { locked = true })

-- Mouse binds (ported from mouse list)
hl.bind(mod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(mod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

--  ── Window Rules: Floating (ported from layouts.py float_rules) ──────────

hl.window_rule({ name = "float-confirmreset", match = { class = "confirmreset" }, float = true })
hl.window_rule({ name = "float-makebranch", match = { class = "makebranch" }, float = true })
hl.window_rule({ name = "float-maketag", match = { class = "maketag" }, float = true })
hl.window_rule({ name = "float-ssh-askpass", match = { class = "ssh-askpass" }, float = true })
hl.window_rule({ name = "float-branchdialog", match = { title = "branchdialog" }, float = true })
hl.window_rule({ name = "float-pinentry", match = { title = "pinentry" }, float = true })
hl.window_rule({
	name = "float-godot-create-folder",
	match = { title = "Create Folder", class = "Godot_Editor" },
	float = true,
})
hl.window_rule({
	name = "float-godot-confirm",
	match = { title = "Please Confirm...", class = "Godot_Editor" },
	float = true,
})
hl.window_rule({
	name = "float-godot-create-node",
	match = { title = "Create New Node", class = "Godot_Editor" },
	float = true,
})
hl.window_rule({ name = "float-flameshot", match = { class = "flameshot" }, float = true })

-- Scratchpad windows: float, center, 80% size
hl.window_rule({ name = "scratch-float", match = { workspace = "^special:(term|btop|volume)$" }, float = true })
hl.window_rule({ name = "scratch-size", match = { workspace = "^special:(term|btop|volume)$" }, size = "80% 80%" })
hl.window_rule({ name = "scratch-center", match = { workspace = "^special:(term|btop|volume)$" }, center = true })

-- Suppress maximize events (ported from qtile auto_fullscreen behavior)
hl.window_rule({
	name = "suppress-maximize",
	match = { class = ".*" },
	suppress_event = "maximize",
})
