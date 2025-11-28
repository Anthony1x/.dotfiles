# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

zstyle ':omz:update' mode auto      # update automatically without asking

# source ~/.zsh/catppuccin_mocha-zsh-syntax-highlighting.zsh

plugins=(
	zsh-autosuggestions
	zsh-syntax-highlighting
	fast-syntax-highlighting
	# zsh-autocomplete
)

source $ZSH/oh-my-zsh.sh
eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/config.toml)"

if [[ "$TERM_PROGRAM" == 'vscode' ]] || [[ "$TERM_PROGRAM" == 'zed' ]] ; then
  alias 'rg'='rg --smart-case --hidden --no-heading --column'
fi

alias xampp="sudo /opt/lampp/xampp"
alias vimconf="/home/anthony/.config/nvim/init.vim"
alias ls="eza"
alias ll="eza -labhSo"
alias sizeof="stat --printf='%s'"
alias man='batman'
alias KILLYOURSELF="exit"
alias yay="paru"
alias fz="fzf --preview 'bat --style=numbers --color=always {}'"
alias cd="z"
alias vim="nvim"


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

export MANPAGER="sh -c 'col -bx | bat -l man -p'"

export PATH=$PATH:/home/anthony/.spicetify
export PATH="$PATH:/home/anthony/.local/bin"

export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow'

export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8

source <(fzf --zsh)

eval "$(zoxide init zsh)"

# Added by `rbenv init` on Wed Apr  2 02:39:55 PM CEST 2025
eval "$(rbenv init - --no-rehash zsh)"
eval "$(fnm env --use-on-cd --shell zsh)"

