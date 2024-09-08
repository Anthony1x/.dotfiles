local on_attach = require("util.lsp").on_attach
local diagnostic_signs = require("util.lsp").diagnostic_signs

local config = function()
    require("neoconf").setup({})
    local cmp_nvim_lsp = require("cmp_nvim_lsp")
    local lspconfig = require("lspconfig")

    for type, icon in pairs(diagnostic_signs) do
        local hl = "DiagnosticSign" .. type
        vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = "" })
    end

    local capabilities = cmp_nvim_lsp.default_capabilities()

    -- lua
    lspconfig.lua_ls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        settings = { -- custom settings for lua
            Lua = {
                -- make the language server recognize "vim" global
                diagnostics = {
                    globals = { "vim" },
                },
                workspace = {
                    -- make language server aware of runtime files
                    library = {
                        [vim.fn.expand("$VIMRUNTIME/lua")] = true,
                        [vim.fn.stdpath("config") .. "/lua"] = true,
                    },
                },
            },
        },
    })

    -- json
    lspconfig.jsonls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        filetypes = { "json", "jsonc" },
    })

    -- typescript
    lspconfig.ts_ls.setup({
        -- Re-enable this block comment once inlay hints are actually supported in neovim
        -- [
        init_options = {
            preferences = {
                includeInlayParameterNameHints = "all",
                includeInlayParameterNameHintsWhenArgumentMatchesName = true,
                includeInlayFunctionParameterTypeHints = true,
                includeInlayVariableTypeHints = true,
                includeInlayPropertyDeclarationTypeHints = true,
                includeInlayFunctionLikeReturnTypeHints = true,
                includeInlayEnumMemberValueHints = true,
                importModuleSpecifierPreference = "non-relative",
            },
        },
        -- ]

        on_attach = on_attach,
        capabilities = capabilities,
        filetypes = {
            "typescript", "javascript"
        },
        root_dir = lspconfig.util.root_pattern("package.json", "tsconfig.json", ".git"),
    })

    -- bash
    lspconfig.bashls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        filetypes = { "sh" },
    })

    -- html, typescriptreact, javascriptreact, css, sass, scss, less, svelte, vue
    lspconfig.emmet_ls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        filetypes = {
            "html",
            "typescriptreact",
            "javascriptreact",
            "javascript",
            "css",
            "sass",
            "scss",
            "less",
            "svelte",
            "vue",
        },
    })

    -- docker
    lspconfig.dockerls.setup({
        capabilities = capabilities,
        on_attach = on_attach,
    })

    -- C / C++
    lspconfig.clangd.setup({
        filetypes = { "c", "cpp", "h", "hpp" },
        on_attach = function(client, bufnr)
            client.server_capabilities.signatureHelpProvider = false
            on_attach(client, bufnr)
            capabilities = capabilities
        end,
    })

    -- php
    lspconfig.intelephense.setup({
        capabilities = capabilities,
        on_attach = on_attach,
        filetypes = { "php" },
    })

    local luacheck = require("efmls-configs.linters.luacheck")
    local stylua = require("efmls-configs.formatters.stylua")
    local flake8 = require("efmls-configs.linters.flake8")
    local black = require("efmls-configs.formatters.black")
    local eslint_d = require("efmls-configs.linters.eslint_d")
    local prettierd = require("efmls-configs.formatters.prettier_d")
    local fixjson = require("efmls-configs.formatters.fixjson")
    local shellcheck = require("efmls-configs.linters.shellcheck")
    local shfmt = require("efmls-configs.formatters.shfmt")
    local alex = require("efmls-configs.linters.alex")
    local hadolint = require("efmls-configs.linters.hadolint")
    local solhint = require("efmls-configs.linters.solhint")
    -- local php = require("efmls-configs.")

    -- configure efm server
    lspconfig.efm.setup({
        filetypes = {
            "lua",
            "python",
            "json",
            "jsonc",
            "sh",
            "javascript",
            "javascriptreact",
            "typescript",
            "typescriptreact",
            "svelte",
            "vue",
            "markdown",
            "docker",
            "solidity",
            "php",
        },
        init_options = {
            documentFormatting = true,
            documentRangeFormatting = true,
            hover = true,
            documentSymbol = true,
            codeAction = true,
            completion = true,
        },
        settings = {
            languages = {
                lua = { luacheck, stylua },
                python = { flake8, black },
                typescript = { eslint_d, prettierd },
                json = { eslint_d, fixjson },
                jsonc = { eslint_d, fixjson },
                sh = { shellcheck, shfmt },
                javascript = { eslint_d, prettierd },
                javascriptreact = { eslint_d, prettierd },
                typescriptreact = { eslint_d, prettierd },
                svelte = { eslint_d, prettierd },
                vue = { eslint_d, prettierd },
                markdown = { alex, prettierd },
                docker = { hadolint, prettierd },
                solidity = { solhint },
                -- php = { php }
            },
        },
    })
end

return {
    "neovim/nvim-lspconfig",
    config = config,
    lazy = false,
    dependencies = {
        "windwp/nvim-autopairs",
        "williamboman/mason.nvim",
        "creativenull/efmls-configs-nvim",
        "hrsh7th/nvim-cmp",
        "hrsh7th/cmp-buffer",
        "hrsh7th/cmp-nvim-lsp",
    },
}
