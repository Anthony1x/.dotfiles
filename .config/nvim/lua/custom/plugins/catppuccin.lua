return {
  'catppuccin/nvim',
  name = 'catppuccin',
  lazy = false,
  priority = 1000, -- Make sure to load this before all the other start plugins.
  config = function()
    -- Neovim keeps 'background' in sync with the terminal's light/dark mode (and kitty follows the OS),
    -- so 'auto' picks the flavour from it and switches whenever it changes.
    require('catppuccin').setup {
      flavour = 'auto',
      background = { light = 'latte', dark = 'mocha' },
    }
    vim.cmd.colorscheme 'catppuccin'
  end,
}
