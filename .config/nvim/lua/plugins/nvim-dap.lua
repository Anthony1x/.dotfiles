return {
    "mfussenegger/nvim-dap",
    dependencies = {
        "mason-org/mason.nvim",
        "jay-babu/mason-nvim-dap.nvim",
        "rcarriga/nvim-dap-ui",
        "nvim-neotest/nvim-nio",
    },
    keys = {
        {
            "<leader>db",
            function()
                require("dap").toggle_breakpoint()
            end,
            desc = "Toggle Breakpoint",
        },
        {
            "<leader>dc",
            function()
                require("dap").continue()
            end,
            desc = "Continue",
        },
        {
            "<leader>di",
            function()
                require("dap").step_into()
            end,
            desc = "Step Into",
        },
        {
            "<leader>do",
            function()
                require("dap").step_over()
            end,
            desc = "Step Over",
        },
        {
            "<leader>dO",
            function()
                require("dap").step_out()
            end,
            desc = "Step Out",
        },
        {
            "<leader>dr",
            function()
                require("dap").repl.open()
            end,
            desc = "Open REPL",
        },
        {
            "<leader>du",
            function()
                require("dapui").toggle()
            end,
            desc = "Toggle DAP UI",
        },
    },
    config = function()
        local dap = require("dap")
        local dapui = require("dapui")

        dapui.setup()

        -- Ensure php-debug-adapter is installed
        require("mason-nvim-dap").setup({
            ensure_installed = { "php" },
            automatic_installation = true,
        })

        -- Configure the PHP adapter
        dap.adapters.php = {
            type = "executable",
            command = "node",
            args = { vim.fn.stdpath("data") .. "/mason/packages/php-debug-adapter/extension/out/phpDebug.js" },
        }

        -- dap.configurations.php = {
        --     {
        --         type = "php",
        --         request = "launch",
        --         name = "Listen for Xdebug",
        --         port = 9003,
        --     },
        -- }

        dap.listeners.before.attach.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.launch.dapui_config = function()
            dapui.open()
        end
        dap.listeners.before.event_terminated.dapui_config = function()
            dapui.close()
        end
        dap.listeners.before.event_exited.dapui_config = function()
            dapui.close()
        end
    end,
}
