#!/bin/zsh

# Wrapper to run rofi with blurred background

/usr/bin/rofi -theme $HOME/.config/rofi/config.rasi $@ &
c=0
while ! xprop -f _KDE_NET_WM_BLUR_BEHIND_REGION 32c -set _KDE_NET_WM_BLUR_BEHIND_REGION 0 -id $(xdotool search -class 'rofi') ; do
	sleep .1 
	c=$((c+1))
	[[ c = 50 ]] && exit; # stop script window didn't appear after 5 seconds
done
