# -*- coding: utf-8 -*-
#     ___  _   _ _
#    / _ \| |_(_) | ___
#   | | | | __| | |/ _ \
#   | |_| | |_| | |  __/
#    \__\_\\__|_|_|\___|
#
#   A customized qtile config by me CaptainEureka
#   Email: captaineureka@gmail.com
#   GitHub: CaptainEureka
#
# The following comments are the copyright and licensing information from the default
# qtile config. Copyright (c) 2010 Aldo Cortesi, 2010, 2014 dequis, 2012 Randall Ma,
# 2012-2014 Tycho Andersen, 2012 Craig Barnes, 2013 horsik, 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.

# IMPORTS
import os
import json
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import qtile, layout, bar, widget, hook
from typing import List  # noqa: F401

# DEFINING SOME VARIABLES
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
alt = "mod1"                                     # Sets Alt key
myTerm = "alacritty"                                 # My terminal of choice
myConfig = "/home/mk/.config/qtile/config.py"    # The Qtile config file location

# KEYBINDINGS
keys = [
    # The essentials
    Key(
        [mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches Terminal'
    ),
    Key(
        [mod, "shift"], "Return",
        lazy.spawn("rofi -show drun -theme appslist"),
        desc='Rofi Run Launcher'
    ),
    Key(
        [mod, "control"], "q",
        lazy.spawn("kill -s USR1 $(pidof deadd-notification-center)"),
        desc='Testing deadd'
    ),
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'
    ),
    Key(
        [mod], "q",
        lazy.window.kill(),
        desc='Kill active window'
    ),
    Key(
        [mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'
    ),
    Key(
        [mod, "shift"], "c",
        lazy.shutdown(),
        desc='Shutdown Qtile'
    ),
    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
        ),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
        ),
    # Move focus to next/prev group
    Key([mod, "control"], "Right",
        lazy.screen.next_group(),
        desc='Move focus to next group'
        ),
    Key([mod, "control"], "Left",
        lazy.screen.prev_group(),
        desc='Move focus to previous group'
        ),
    # Window controls
    Key(
        [mod], "k",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
    ),
    Key(
        [mod], "j",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        desc='Move windows down in current stack'
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_up(),
        desc='Move windows up in current stack'
    ),
    Key(
        [mod], "h",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
    ),
    Key(
        [mod], "l",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
    ),
    Key(
        [mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
    ),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
    ),
    # Stack controls
    Key(
        [mod, "shift"], "space",
        lazy.layout.toggle_floating(),
        desc='toggle floating'
    ),
    # Key(
    #     [mod, "shift"], "space",
    #     lazy.layout.rotate(),
    #     lazy.layout.flip(),
    #     desc='Switch which side main pane occupies (XmonadTall)'
    # ),
    # Key(
    #     [mod], "space",
    #     lazy.layout.next(),
    #     desc='Switch window focus to other pane(s) of stack'
    # ),
    Key(
        [mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),
    # Rofi scripts launched with ALT + CTRL + KEY
    Key(
        [alt, "control"], "w",
        lazy.spawn("setbg /home/mk/Pictures/wallpapers"),
        desc='Set wallpaper with Sxiv and xwallpaper'
    ),
    Key(
        [alt, "control"], "b",
        lazy.spawn("bwmenu"),
        desc='Bitwarden menu with Rofi'
    ),
    Key(
        [alt, "control"], "p",
        lazy.spawn("rofi-powermenu"),
        desc='Rofi power menu (shutdown, reboot, lock, logoff)'
    ),
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc='Raise volume 5%'
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc='Lower volume 5%'
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer sset Master toggle"),
        desc='Toggle audio mute'
    ),
    Key(
        [], "Print",
        lazy.spawn("rofi-maim"),
        desc='Rofi screenshot utility'
    ),
    Key(
        [], "XF86MonBrightnessUp",
        lazy.spawn("light -A 10"),
        desc='Increase Brightness'
    ),
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("light -U 10"),
        desc='Decrease Brightness'
    )
]

# GROUPS
group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

# COLORS
def init_colors():
    themefile = os.path.expanduser("~/.cache/pal/themefile")
    with open(themefile) as t:
        theme = t.read()
    theme_dir = os.path.expanduser("~/.config/pal/"+theme+".json")
    with open(theme_dir) as c:
        colors = json.load(c)

    return colors


def recolor_icons(icons, fg):
    icon_dir = os.path.expanduser("~/.config/qtile/icons/")
    for icon in icons:
        subprocess.call(["recolor {} \"{}\"".format(icon_dir+icon,fg)], shell=True)

    return

colors = init_colors()
special_colors = colors['special']
normal_colors = colors['colors']

icons = ["layout-floating.png",
         "layout-max.png",
         "layout-monadtall.png"]

recolor_icons(icons, special_colors['foreground'])

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {"border_width": 4,
                "margin": 24,
                "border_focus": normal_colors['color0'],
                "border_normal": special_colors['background']
                }

# THE LAYOUTS
layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(ratio=1.5, fair=False, lower_right=True, **layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

# DEFAULT WIDGET SETTINGS

fontconfig = {
    "mono": "SF Mono",
    "text": "SF Pro Text",
    "icon": "Feather"
}
widget_defaults = dict(
    font=fontconfig['text'],
    fontsize=24,
    padding=4,
    background=special_colors['foreground']
)
extension_defaults = widget_defaults.copy()

# WIDGETS

def run_eww():
    qtile.cmd_spawn('eww open-many blur_command clock-window battery-window volume-window brightness-window music-window systemctl-window')


def close_eww():
    qtile.cmd_spawn('eww close-all')


def init_widgets():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=special_colors['foreground'],
            background=special_colors['background']
        ),
        widget.TextBox(
            background=special_colors['background'],
            foreground=special_colors['foreground'],
            text="",
            padding=20,
            fontsize=34,
            font=fontconfig['icon'],
            mouse_callbacks={'Button1': run_eww,
                             'Button3': close_eww}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=special_colors['foreground'],
            background=special_colors['background']
        ),
        widget.GroupBox(
            font=fontconfig['icon'],
            fontsize=34,
            padding=20,
            borderwidth=3,
            active=normal_colors['color4'],
            inactive=normal_colors['color8'],
            rounded=True,
            center_aligned=True,
            highlight_color=normal_colors['color0'],
            highlight_method="block",
            this_current_screen_border=normal_colors['color0'],
            this_screen_border=normal_colors['color0'],
            foreground=special_colors['foreground'],
            background=special_colors['background']
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=special_colors['foreground'],
            background=special_colors['background']
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=special_colors['foreground'],
            background=special_colors['background'],
            padding=0,
            scale=0.9
        ),
        widget.Spacer(
            background=special_colors['background']
        ),
        widget.WidgetBox(widgets=[
            widget.TextBox(
                text="VOL:",
                background=special_colors['background'],
                foreground=special_colors['foreground'],
            ),
            widget.Volume(
                background=special_colors['background'],
                foreground=special_colors['foreground'],
                padding=10,
                step=5,
            ),
            widget.Battery(
                background=special_colors['background'],
                foreground=special_colors['foreground'],
                format='BAT: {percent:2.0%}',
                padding=5
            )],
            background=special_colors['background'],
            foreground=special_colors['foreground'],
            close_button_location='right',
            font=fontconfig['icon'],
            fontsize= 38,
            text_closed='  ',
            text_open='  '
        ),
        widget.Systray(
            background=special_colors['background'],
            icon_size=38,
            padding=8
        ),
        widget.Sep(
            linewidth=0,
            padding=20,
            foreground=special_colors['background'],
            background=special_colors['background'],
            size_percent=80
        ),
        widget.Clock(
            foreground=special_colors['foreground'],
            background=special_colors['background'],
            font=fontconfig['text']+" Bold",
            padding=10,
            format="%A %d, %H:%M"
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=special_colors['foreground'],
            background=special_colors['background']
        )
    ]
    return widgets_list


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets(),
                               opacity=0.85,
                               size=64,
                               margin=[10,24,0,24])
                   )]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets()

##### DRAG FLOATING WINDOWS #####
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wmclass': 'zenity'},
    {'wname': 'eww'},
    {'wname': 'sxiv'},
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
],
    border_width=0)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### STARTUP APPLICATIONS #####

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
