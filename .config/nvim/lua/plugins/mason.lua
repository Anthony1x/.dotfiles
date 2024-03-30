return {
    "williamboman/mason.nvim",
    cmd = "Mason",
    event = "BufReadPre",
	  opts = {
		  ensure_installed = {
			  "clangd",
        "clang-format",
        "codelldb",
        "intelephense"
    }
  },
	  config = function()
	    require("mason").setup()
	  end
}
