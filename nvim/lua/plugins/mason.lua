return {
    "williamboman/mason.nvim",
    cmd = "Mason",
    event = "BufReadPre",
	  opts = {
		  ensure_installed = {
			  "clang", "intelephense"	
		  }
	  },
	  config = function()
	    require("mason").setup()
	  end
}
