local mapkey = require("util.keymapper").mapkey

return {
    'nvim-telescope/telescope.nvim', tag = '0.1.6',
      dependencies = { 'nvim-lua/plenary.nvim' },
      lazy = false,
      keys = {
        mapkey("<leader>fk", "Telescope keymaps", "n"),
        mapkey("<leader>fh", "Telescope help_tags", "n"),
        mapkey("<leader>ff", "Telescope find_files", "n"),
        mapkey("<leader>fg", "Telescope live_grep", "n"),
        mapkey("<leader>fb", "Telescope buffers", "n"),
      },
}
