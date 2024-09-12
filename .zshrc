export PATH=$PATH:/home/anthony/.spicetify
export PATH=$PATH:/home/anthony/.local/bin

eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/config.toml)"

if [[ "$TERM_PROGRAM" == 'vscode' ]] || [[ "$TERM_PROGRAM" == 'zed' ]] ; then
  alias 'rg'='rg --smart-case --hidden --no-heading --column'
fi

alias yay="paru"
alias ls="eza"
alias ll="eza -labhSo"
alias sizeof="stat --printf='%s'"
alias man='batman'
alias KILLYOURSELF="exit"

source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh

SAVEHIST=5000  # Save most-recent 5000 lines
HISTFILE=~/.zsh_history
