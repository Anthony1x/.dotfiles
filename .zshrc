export ZSH="$HOME/.oh-my-zsh"

source $ZSH/oh-my-zsh.sh
source ~/.zsh/catppuccin_mocha.zsh

export PATH=$PATH:/home/anthony/.spicetify
export PATH=$PATH:/home/anthony/.local/bin

plugins=(git)

eval "$(oh-my-posh init zsh --config $HOME/.config/ohmyposh/config.toml)"

GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
SDL_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx

GTK_THEME=Adwaita:dark
QT_QPA_PLATFORMTHEME=qt5ct:qt6ct

source ~/.zsh/catppuccin_mocha.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
