-- local null_ls = require('none-ls')

return {
    'nvimtools/none-ls.nvim',
    event = "VeryLazy",
    opts = function ()
        return require "config.null-ls"
    end
}
