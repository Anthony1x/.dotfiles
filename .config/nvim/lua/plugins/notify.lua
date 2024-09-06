return {
    'rcarriga/nvim-notify',
    config = function ()
        require('notify').setup({
            -- level = 'WARN',
            --end_col = 20; --vim.opt.columns:get() - neotree_width
            background_colour = "#000000"
        })
    end
}

