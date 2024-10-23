return {
    "catppuccin/nvim",
    name = "catppuccin",
    lazy = false,
    priority = 999,
    config = function()
        if not vim.g.neovide then
            require("catppuccin").setup({
                transparent_background = true,
            })
        end
        vim.cmd("colorscheme catppuccin-mocha")
    end,
}
