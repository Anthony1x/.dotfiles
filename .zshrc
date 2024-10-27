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

