#!/bin/bash

function show_apps() {
  ICON_CODE="\0icon\x1f"
  echo -e "Code"$ICON_CODE"code"
  echo -e "IntelliJ"$ICON_CODE"intellij"
  echo -e "Atom"$ICON_CODE"atom"
  echo -e "Geany"$ICON_CODE"geany"
  echo -e "Neovim"$ICON_CODE"nvim"
  echo -e "Vim"$ICON_CODE"vim"
  echo -e "Emacs"$ICON_CODE"emacs"
  echo -e "Qt5 Assistant"$ICON_CODE"assistant"
}

function show_rofi() {
  # show_apps | rofi -modi "" -show combi -theme concept -dmenu -mesg "Development"
  rofi -modi apps -show apps:show_apps -theme concept -dmenu -mesg "Development"
}

selection=$(show_rofi)
echo $selection

if [[ ! -z $selection ]]; then
  notify-send "Running..." $selection
fi
