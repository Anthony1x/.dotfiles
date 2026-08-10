return {
  'olimorris/codecompanion.nvim',
  dependencies = {
    'nvim-lua/plenary.nvim',
    'nvim-treesitter/nvim-treesitter',
  },
  config = function()
    require('codecompanion').setup {
      interactions = {
        chat = {
          -- You can specify an adapter by name and model (both ACP and HTTP)
          adapter = {
            name = 'anthropic',
            model = 'Opus',
          },
        },
      },
    }
  end,
}
