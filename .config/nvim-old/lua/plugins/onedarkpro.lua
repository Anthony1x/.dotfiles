return {
    "olimorris/onedarkpro.nvim",
    name = "odp",
    lazy = false,
    priority = 1000,
    config = function()
        local odp = require("onedarkpro").setup {
            colors = {
                dark = { bg = "#1E1E2E" },
            }
        }
        -- vim.cmd("colorscheme onedark_vivid")
    end
}
