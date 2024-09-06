local mapkey = require("util.keymapper").mapkey
-- local wk = require("which-key")

local toggle = "Neotree toggle"
local focus = "Neotree focus"

-- Directory Navigation
mapkey("<leader>m", focus, "n")
mapkey("<leader>e", toggle, "n")

-- Window Management
mapkey("<leader>sv", "vsplit", "n") -- Split Vertically
mapkey("<leader>sh", "split", "n") -- Split Horizontally
mapkey("<leader>sm", "MaximizerToggle", "n") -- Toggle Minimise

-- DAP
mapkey("<leader>db", "DapToggleBreakpoint<CR>", "n")
mapkey("<leader>dr", "DapContinue<CR>", "n")

-- Format
mapkey("<leader>fm", ":lua vim.lsp.buf.format()<CR>", "n")

-- wk.add({
-- 	{ "<leader>fm",":lua vim.lsp.buf.format()<CR>", "Format", "n" },
-- })
