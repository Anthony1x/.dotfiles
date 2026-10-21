#!/bin/sh

# Shells export this as THEME_MODE before each prompt (precmd in ~/.zshrc);
# oh-my-posh picks its latte/mocha palette from it.
case "$1" in
    dark | light) ;;
    *) exit 0 ;; # "null" when darkman starts without a location
esac

mkdir -p ~/.local/state
echo "$1" > ~/.local/state/theme-mode
