local config = function()
	local theme = require("lualine.themes.catppuccin")
    local gitblame = require('gitblame')

	-- set bg transparency in all modes
	--theme.normal.c.bg = nil
	--theme.insert.c.bg = nil
	--theme.visual.c.bg = nil
	--theme.replace.c.bg = nil
	--theme.command.c.bg = nil

	require("lualine").setup({
		options = {
			theme = theme,
			globalstatus = true,
            section_separators = { left = '', right = '' },
            component_separators = '',
		},
		sections = {
			lualine_a = { "mode" },
			-- lualine_b = { "buffers" },
            lualine_x = {{ gitblame.get_current_blame_text, cond = gitblame.is_blame_text_available }},
			lualine_y = { "fileformat", "filetype" },
			lualine_z = { "progress", "location" },
		},
		-- tabline = {},
	})
end

return {
	"nvim-lualine/lualine.nvim",
	lazy = false,
	config = config,
}
