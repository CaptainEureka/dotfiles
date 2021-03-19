#!/usr/bin/env bash

if ps -C spotify > /dev/null; then
    PLAYER="spotify"
elif ps -C spotifyd > /dev/null; then
    PLAYER="spotifyd"
elif ps -C mopidy > /dev/null; then
    PLAYER="mopidy"
fi

STATUS="Nothing"
TITLE="Not Playing"
ARTIST="--"
ALBUM="/ --"

if [ "$PLAYER" = "spotify" ] || [ "$PLAYER" = "spotifyd" ] || [ "$PLAYER" = "mopidy" ]; then
    ARTIST=$(playerctl metadata --format '{{ artist }}')
    ALBUM=$(playerctl metadata --format '{{ album }}')
    TITLE=$(playerctl metadata --format '{{ title }}')
    STATUS=$(playerctl -p $PLAYER status)
fi 

if [ "$STATUS" = "Playing" ]; then
    STATUS=""
else
    STATUS=""
fi

# download album art
artUrl=$(playerctl metadata mpris:artUrl)
if [ "$artUrl" == "No player could handle this command" ] && [ "$1" ]; then
    cp ~/.config/eww/images/vinyl-placeholder-nord.png /tmp/cover.png
else
    curl -s "$artUrl" --output /tmp/cover.png
fi

# update eww if it's running
eww update title="$TITLE"
eww update artist-album="$ARTIST"
eww update mus-status="$STATUS"
echo " "
