# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

zstyle ':omz:update' mode auto

plugins=(
	zsh-autosuggestions
	zsh-syntax-highlighting
	fast-syntax-highlighting
	# zsh-autocomplete
)

source $ZSH/oh-my-zsh.sh
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/config.toml)"

# Light/dark palette for oh-my-posh (see palettes in its config). Must run
# before _omp_precmd, which renders the prompt, hence prepended.
_theme_mode_precmd() {
  [[ -r ~/.local/state/theme-mode ]] && export THEME_MODE=$(<~/.local/state/theme-mode)
}
precmd_functions=(_theme_mode_precmd $precmd_functions)

if [[ "$TERM_PROGRAM" == 'vscode' ]] || [[ "$TERM_PROGRAM" == 'zed' ]] ; then
  alias 'rg'='rg --smart-case --hidden --no-heading --column'
fi

alias ls="eza"
alias ll="eza -labhSo"
alias cd="z"
alias sizeof="stat --printf='%s'"
alias man='batman'
alias KILLYOURSELF="exit"
alias brexit="exit"
alias yay="paru"
alias fz="fzf --preview 'bat --style=numbers --color=always {}'"
alias vim="nvim"
alias sudo="sudo-rs"
alias sudoedit="sudoedit-rs"
alias claude="claude --allow-dangerously-skip-permissions"
alias clear="pyroclear"

alias dcu="docker compose up -d"
alias dcul="docker compose up -d & lazydocker"

fcd() { cd "$(find . -type d -not -path '*/.*' | fzf)" && l; }
f() { echo "$(find . -type f -not -path '*/.*' | fzf)" | pbcopy }
fv() { nvim "$(find . -type f -not -path '*/.*' | fzf)" }

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}

# Function to mount a remote directory using sshfs
acefs() {
    local remote="$1"
    local local_dir="$HOME/Documents/link"

    # Create the local directory if it doesn't exist
    mkdir -p "$local_dir"

    # Mount the remote directory
    sshfs "$remote" "$local_dir"
}

# Command runs detached from the terminal
spawn() {
    local command="$1"

    setsid "$command" & disown
}

export MANPAGER="sh -c 'col -bx | bat -l man -p'"

export PATH=$PATH:/home/anthony/.spicetify
export PATH="$PATH:/home/anthony/.local/bin"
export PATH="$HOME/.cargo/bin:$PATH"

export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow'

export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8

export EDITOR="nvim"
export SUDO_EDITOR="nvim"

source <(fzf --zsh)

eval "$(zoxide init zsh)"

# Added by `rbenv init` on Wed Apr  2 02:39:55 PM CEST 2025
eval "$(rbenv init - --no-rehash zsh)"
eval "$(fnm env --use-on-cd --shell zsh)"


# SSH agent socket (managed by systemd user ssh-agent.socket)
export SSH_AUTH_SOCK="${XDG_RUNTIME_DIR}/ssh-agent.socket"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Claude Code sources this file into its own shell and sets CLAUDECODE=1.
# Give it back the plain `cd` builtin: anything that shadows cd (zoxide's
# `--cmd cd`, an alias) makes the agent fuzzy-jump to some other directory
# instead of failing on a bad path. Keep this last so it wins over every init
# above. `z` and the rest of the aliases stay available to the agent.
if [[ -n "$CLAUDECODE" ]]; then
  unalias cd 2>/dev/null
  unfunction cd 2>/dev/null
fi
