#!/usr/bin/env bash

icon_dir="${HOME}/.config/qtile/icons"
color="$1"

cd $icon_dir
icons=$(ls | grep '^.*.svg$')

function recolor_icon() {
    sed -E 's/#[0-9A-Fa-f]{6}/'${2}'/g' ${1} | inkscape --pipe --export-filename=$(echo ${1} | sed 's/svg/png/g') &>/dev/null
}

for icon in ${icons}; do
  recolor_icon ${icon} ${color}
done
