export PATH=$PATH:/home/anthony/.spicetify
export PATH=$PATH:/home/anthony/.local/bin

# The only real reason I use oh-my-zsh is because of the sane defaults.
# I never knew what a pain zsh is without it.
# Have you ever tried deleting something with 'Del'?
# This shit sucks man. I'll look into fish in the future
export ZSH="$HOME/.oh-my-zsh"
source $ZSH/oh-my-zsh.sh

eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/config.toml)"

if [[ "$TERM_PROGRAM" == 'vscode' ]] || [[ "$TERM_PROGRAM" == 'zed' ]] ; then
  alias 'rg'='rg --smart-case --hidden --no-heading --column'
fi

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh

alias yay="paru"
alias ls="eza"
alias ll="eza -labhSo"
alias sizeof="stat --printf='%s'"
alias man='batman'
alias KILLYOURSELF="exit"
alias fz="fzf --preview 'bat --style=numbers --color=always {}'"
alias qr='qrencode -m 2 -t utf8 <<< "$1"'

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

export MANPAGER="sh -c 'col -bx | bat -l man -p'"


export FZF_DEFAULT_COMMAND='fd --type f --hidden --follow'

source <(fzf --zsh)
