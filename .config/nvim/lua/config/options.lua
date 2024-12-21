local opt = vim.opt

TABSIZE = 4

-- Tab / Indentation
opt.tabstop = TABSIZE
opt.shiftwidth = TABSIZE
opt.softtabstop = TABSIZE
opt.expandtab = true
opt.smartindent = true
opt.wrap = false

-- Disable animations
vim.g.snacks_animate = false

vim.api.nvim_set_option_value("colorcolumn", "120", {})

local augroup = vim.api.nvim_create_augroup("numbertoggle", {})

vim.api.nvim_create_autocmd({ "BufEnter", "FocusGained", "InsertLeave", "CmdlineLeave", "WinEnter" }, {
    pattern = "*",
    group = augroup,
    callback = function()
        if vim.o.nu and vim.api.nvim_get_mode().mode ~= "i" then
            vim.opt.relativenumber = true
        end
    end,
})

vim.api.nvim_create_autocmd({ "BufLeave", "FocusLost", "InsertEnter", "CmdlineEnter", "WinLeave" }, {
    pattern = "*",
    group = augroup,
    callback = function()
        if vim.o.nu then
            vim.opt.relativenumber = false
            vim.cmd("redraw")
        end
    end,
})

WINBLEND = 0

if vim.g.neovide then
    vim.g.neovide_window_blurred = true
    vim.g.neovide_scroll_animation_length = 0.1
    WINBLEND = 20
end

vim.opt.winblend = WINBLEND
