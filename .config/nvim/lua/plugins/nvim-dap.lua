return {
    "mfussenegger/nvim-dap",
    config = function()
        local dap = require("dap")

        -- dap.adapters.php = {
        -- 	type = "executable",
        -- 	command = "node",
        -- 	args = { os.getenv("HOME") .. "/vscode-php-debug/out/phpDebug.js" },
        -- }

        dap.configurations.php = {
            {
                type = "php",
                request = "launch",
                name = "Listen for xdebug",
                port = "9003",
                log = true,
                serverSourceRoot = "/srv/app",
                localSourceRoot = "~/Documents/Dev/Typo3/bauwirtschaft-bw.de/app",
            },
            {
                name = "Launch currently open script",
                type = "php",
                request = "launch",
                program = "${file}",
                cwd = "${fileDirname}",
                port = 0,
                env = {
                    XDEBUG_MODE = "debug,develop",
                    XDEBUG_CONFIG = "client_port=${port}",
                },
                runtimeArgs = {
                    "-dxdebug.start_with_request=yes",
                },
            },
        }
    end,
}
