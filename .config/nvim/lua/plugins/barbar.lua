return {
  "romgrk/barbar.nvim",
  lazy = false,
  dependencies = {
    'nvim-tree/nvim-web-devicons',   -- OPTIONAL: for file icons
  },
  init = function()
    vim.g.barbar_auto_setup = true   -- false
  end
}
