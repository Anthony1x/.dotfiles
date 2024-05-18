return {
  "mfussenegger/nvim-dap",
  opts = function ()
    return {
      adapters = {
        lldb = {
          type = 'executable',
          command = '/usr/bin/lldb-vscode',
          name = 'lldb'
        }
      }
    }
  end
}
