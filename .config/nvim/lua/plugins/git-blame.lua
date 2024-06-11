return {
  'f-person/git-blame.nvim',
    config = function()
      -- import nvim-treesitter plugin
      local gitblame = require('gitblame')

        gitblame.setup {
            date_format = '%d %b %Y, %H:%M',
            display_virtual_text = 0
        }

    end
}
