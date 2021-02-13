#!/usr/bin/env bash 

function run_once {
  if [ ! $(pgrep -f $1) ];
  then
    $@ &
  fi
}

run_once picom --experimental-backends --config ~/.config/qtile/configuration/picom.conf
run_once nm-applet --no-agent
run_once mopidy
run_once eww daemon
run_once libinput-gestures -c ~/.config/qtile/configuration/libinput-gestures.conf
launch-dunst
setbg -r
