#!/usr/bin/env bash 

function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}

# run deadd-notification-center
run picom --experimental-backends --config ~/.config/qtile/configuration/picom.conf
run nm-applet --no-agent
xob-volume-watcher.py | xob -s gruvbpx &
setbg -r
run mopidy
# run libinput-gestures
