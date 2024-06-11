local mapkey = require("util.keymapper").mapkey

-- Directory Navigation
mapkey("<leader>m", "NvimTreeFocus", "n")
mapkey("<leader>e", "NvimTreeToggle", "n")

-- Window Management
mapkey("<leader>sv", "vsplit", "n") -- Split Vertically
mapkey("<leader>sh", "split", "n") -- Split Horizontally
mapkey("<leader>sm", "MaximizerToggle", "n") -- Toggle Minimise

-- DAP
mapkey("<leader>db", "DapToggleBreakpoint<CR>", "n")
mapkey("<leader>dr", "DapContinue<CR>", "n")
