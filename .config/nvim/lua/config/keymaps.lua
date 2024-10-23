-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- use `vim.keymap.set` instead
local map = vim.keymap.set

-- Enable inlay hint support
map("n", "<leader>uh", function()
    vim.lsp.inlay_hint(0, nil)
end, { desc = "Toggle inlay hints" })
