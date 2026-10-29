# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# macOS: Homebrew onto PATH before anything below calls brew-installed tools
if [[ "$OSTYPE" == darwin* && -x /opt/homebrew/bin/brew ]]; then
  eval "$(/opt/homebrew/bin/brew shellenv)"
fi

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
# Linux: darkman writes ~/.local/state/theme-mode. macOS: read the system appearance.
_theme_mode_precmd() {
  if [[ -r ~/.local/state/theme-mode ]]; then
    export THEME_MODE=$(<~/.local/state/theme-mode)
  elif [[ "$OSTYPE" == darwin* ]]; then
    [[ "$(defaults read -g AppleInterfaceStyle 2>/dev/null)" == Dark ]] && export THEME_MODE=dark || export THEME_MODE=light
  fi
}
precmd_functions=(_theme_mode_precmd $precmd_functions)

if [[ "$TERM_PROGRAM" == 'vscode' ]] || [[ "$TERM_PROGRAM" == 'zed' ]] ; then
  alias 'rg'='rg --smart-case --hidden --no-heading --column'
fi

alias ls="eza"
alias ll="eza -labhSo"
alias cd="z"
alias man='batman'
alias KILLYOURSELF="exit"
alias brexit="exit"
alias fz="fzf --preview 'bat --style=numbers --color=always {}'"
alias vim="nvim"
alias claude="claude --allow-dangerously-skip-permissions"

if [[ "$OSTYPE" == linux* ]]; then
  alias sizeof="stat --printf='%s'"
  alias yay="paru"
  alias sudo="sudo-rs"
  alias sudoedit="sudoedit-rs"
  alias clear="pyroclear"
else
  alias sizeof="stat -f %z"
  alias sudoedit="sudo -e"
fi

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

# Command runs detached from the terminal (macOS has no setsid)
spawn() {
    local command="$1"

    if (( $+commands[setsid] )); then
        setsid "$command" & disown
    else
        "$command" &>/dev/null & disown
    fi
}

export MANPAGER="sh -c 'col -bx | bat -l man -p'"

export PATH="$PATH:$HOME/.spicetify"
export PATH="$PATH:$HOME/.local/bin"
export PATH="$HOME/.cargo/bin:$PATH"

export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow'

export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8

export EDITOR="nvim"
export SUDO_EDITOR="nvim"

(( $+commands[fzf] )) && source <(fzf --zsh)

(( $+commands[zoxide] )) && eval "$(zoxide init zsh)"

# Added by `rbenv init` on Wed Apr  2 02:39:55 PM CEST 2025
(( $+commands[rbenv] )) && eval "$(rbenv init - --no-rehash zsh)"
(( $+commands[fnm] )) && eval "$(fnm env --use-on-cd --shell zsh)"


# SSH agent socket (managed by systemd user ssh-agent.socket); macOS brings its own via launchd
if [[ "$OSTYPE" == linux* ]]; then
  export SSH_AUTH_SOCK="${XDG_RUNTIME_DIR}/ssh-agent.socket"
fi

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Claude Code sources this file into its own shell and sets CLAUDECODE=1.
# Give it back the plain builtins/binaries. Anything that shadows these breaks
# the agent in ways that look like a failing command instead of a bad alias:
#   cd -> zoxide's `--cmd cd` or an alias makes it fuzzy-jump to some other
#         directory instead of failing on a bad path.
#   ls -> eza blocks forever reading stdin when it follows a heredoc in the same
#         command. The call "times out" and is backgrounded although the real
#         work already succeeded, so the obvious fix (rerun) just adds another
#         stuck process.
# Keep this last so it wins over every init above. `z`, `eza` and the rest stay
# available to the agent under their own names.
if [[ -n "$CLAUDECODE" ]]; then
  unalias cd 2>/dev/null
  unfunction cd 2>/dev/null
  unalias ls 2>/dev/null
  unalias ll 2>/dev/null
fi
