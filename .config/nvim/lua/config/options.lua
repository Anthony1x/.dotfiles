-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

TABSIZE = 4

-- Tab / Indentation
vim.o.tabstop = TABSIZE -- A TAB character looks like 4 spaces
vim.o.expandtab = true -- Pressing the TAB key will insert spaces instead of a TAB character
vim.o.softtabstop = TABSIZE -- Number of spaces inserted instead of a TAB character
vim.o.shiftwidth = TABSIZE -- Number of spaces inserted when indenting

vim.api.nvim_set_option_value("colorcolumn", "120", {})

vim.g.snacks_animate = false
