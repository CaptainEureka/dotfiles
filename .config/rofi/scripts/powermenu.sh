#!/bin/bash

rofi_command="rofi -no-config -theme ../themes/powermenu.rasi"

### Options ###
power_off=""
reboot=""
lock=""
suspend="⏾"
log_out="﫼"
# Variable passed to rofi
options="$power_off\n$reboot\n$lock\n$suspend\n$log_out"

chosen="$(echo -e "$options" | $rofi_command -dmenu -selected-row 2)"
case $chosen in
    $power_off)
        systemctl poweroff
        ;;
    $reboot)
        systemctl reboot
        ;;
    $lock)
        betterlockscreen -l blur
        ;;
    $suspend)
        mpc -q pause
        amixer set Master mute
        systemctl suspend
        ;;
    $log_out)
        i3exit logout
        ;;
esac

