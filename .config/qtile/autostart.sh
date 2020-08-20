#!/usr/bin/env bash 

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

# run deadd-notification-center
run picom -b --experimental-backends --config ~/.config/qtile/configuration/picom.conf
run nm-applet --no-agent
xob-volume-watcher.py | xob &
setbg -r
# run libinput-gestures
