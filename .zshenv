#FZF x PyWal
source ~/.cache/wal/colors.sh
export FZF_DEFAULT_OPTS=""
export FZF_DEFAULT_OPTS="
       $FZF_DEFAULT_OPTS
       --color fg:$foreground,hl:$color4,fg+:$color7,bg+:$color8,hl+:$color11
       --color info:$color7,prompt:$color2,spinner:$color1,pointer:$color11,marker:$color1
"
