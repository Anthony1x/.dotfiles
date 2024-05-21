return {
  'nvimtools/none-ls.nvim',
  event = "VeryLazy",
  opts = function ()
    local none_ls = require 'null-ls'
    local autogroup = vim.api.nvim_create_augroup('LspFormatting', {})
    return {
      sources = { none_ls.builtins.formatting.clang_format },
      on_attach = function (client,bufnr)
        if client.supports_method("textDocument/formatting") then
          vim.api.nvim_clear_autocmds({
        group = autogroup,
        buffer = bufnr
      })
      vim.api.nvim_create_autocmd("BufWritePre", {
        group = autogroup,
        buffer = bufnr,
        callback = function ()
          vim.lsp.buf.format({ bufnr = bufnr})
        end
      })
    end
  end,
    }
 end
}