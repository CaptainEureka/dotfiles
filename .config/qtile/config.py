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
from datetime import date
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import qtile, layout, bar, widget, hook
from libqtile.command.client import CommandClient
c = CommandClient()
from typing import List  # noqa: F401

# DEFINING SOME VARIABLES
mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
alt = "mod1"                                     # Sets Alt key
myTerm = "kitty"                                 # My terminal of choice
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
        lazy.spawn("rofi -show drun -modi drun,file-browser,window,run -theme appslist"),
        desc='Rofi Run Launcher'
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
    Key(
        [mod, "shift"], "e",
        lazy.hide_show_bar(),
        desc='Toggle bar'
    ),
    # Switch focus of monitors
    Key(
        [mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
    ),
    Key(
        [mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
    ),
    # Move focus to next/prev group
    Key(
        [mod, "control"], "Right",
        lazy.screen.next_group(),
        desc='Move focus to next group'
    ),
    Key(
        [mod, "control"], "Left",
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
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
    ),
    Key(
        [mod, "control"], "Return",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
    ),
    # Rofi scripts launched with ALT + CTRL + KEY
    Key([alt, "control"], "e",
        lazy.spawn("eww close-all"),
        desc='Just in case I screw up Eww'
    ),
    Key(
        [alt, "control"], "w",
        lazy.spawn("setbg /home/mk/Downloads"),
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
    # Media Keys
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer sset Master 5%+"),
        desc='Raise volume'
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer sset Master 5%-"),
        desc='Lower volume'
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer sset Master toggle"),
        desc='Toggle audio mute'
    ),
    Key(
        [], "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc='Next track'
    ),
    Key(
        [], "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc='Previous track'
    ),
    Key(
        [], "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc='Play/Pause track'
    ),
    Key(
        [], "XF86AudioStop",
        lazy.spawn("playerctl stop"),
        desc='Stop track'
    ),
    Key(
        [], "Print",
        lazy.spawn("rofi-maim"),
        desc='Rofi screenshot utility'
    ),
    # Monitor Brightness
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
    theme_dir = os.path.expanduser("~/.config/pal/{}.json".format(theme))
    with open(theme_dir) as c:
        colors = json.load(c)

    return colors

colors = init_colors()
theme_colors = colors['special'] | colors['colors']

# a DPI function not unlike that found in AwesomeWM 
def dpi(value):
    Xresources = os.path.expanduser("~/.Xresources")
    with open(Xresources) as X:
        xrdb = X.readlines()

    dpi = 96
    for line in xrdb:
        if re.search('dpi',line):
            dpi = line.split(':')[1].strip()

    return int(value * int(dpi) / 96)

# DEFAULT THEME SETTINGS FOR LAYOUTS
layout_theme = {"border_width": dpi(2),
                "margin": dpi(11),
                "border_focus": theme_colors['color4'],
                "border_normal": theme_colors['color8']
                }

# THE LAYOUTS
layouts = [
    # layout.MonadWide(**layout_theme),
    # layout.Bsp(ratio=1.5, fair=True, lower_right=False, **layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
]

# DEFAULT WIDGET SETTINGS

fontconfig = {
    "mono": "Monaco",
    "text": "Inter",
    "icon": "Feather"
}
widget_defaults = dict(
    font=fontconfig['text'],
    fontsize=11,
    padding=dpi(4),
    foreground=theme_colors['foreground'],
    background=theme_colors['background']
)
extension_defaults = widget_defaults.copy()

# WIDGETS

def toggle_eww_ctl_window():
    qtile.cmd_spawn('eww-toggle ctl-window ')

def toggle_eww_calendar():
    qtile.cmd_spawn('eww-toggle calendar-widget')

def run_rofi():
    qtile.cmd_spawn('rofi -show drun -modi drun,file-browser,window,run -theme appslist')

def day_suffix():
    today = date.today()
    day = int(today.strftime("%-d"))

    suffix = ["th", "st", "nd", "rd"]
    if day % 10 in (1,2,3) and day not in (11,12,13):
        return suffix[day % 10]
    else:
        return suffix[0]

def init_widgets():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=theme_colors['foreground'],
            background=theme_colors['background']
        ),
        widget.TextBox(
            background=theme_colors['background'],
            foreground=theme_colors['foreground'],
            text="",
            font=fontconfig['icon'],
            padding=10,
            fontsize=18,
            mouse_callbacks={'Button1': toggle_eww_ctl_window}
        ),
        widget.TextBox(
            background=theme_colors['background'],
            foreground=theme_colors['foreground'],
            text="",
            font=fontconfig['icon'],
            padding=10,
            fontsize=18,
            mouse_callbacks={'Button1': run_rofi}
        ),
        widget.Sep(
            linewidth=2,
            padding=6,
            size_percent=60,
            foreground=theme_colors['color8'],
            background=theme_colors['background']
        ),
        widget.Sep(
            linewidth=0,
            padding=12,
            foreground=theme_colors['foreground'],
            background=theme_colors['background']
        ),
        widget.GroupBox(
            active=theme_colors['foreground'],
            background=theme_colors['background'],
            block_highlight_text_color=theme_colors['background'],
            borderwidth=2,
            center_aligned=True,
            font=fontconfig['icon'],
            fontsize=18,
            foreground=theme_colors['foreground'],
            highlight_color=theme_colors['color4'],
            highlight_method="block",
            inactive=theme_colors['color8'],
            margin=3,
            padding=6,
            rounded=True,
            this_current_screen_border=theme_colors['color4'],
            this_screen_border=theme_colors['color0'],
            urgent_alert_method="block",
            urgent_border=theme_colors['color1'],
            urgent_text=theme_colors['background']
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=theme_colors['foreground'],
            background=theme_colors['background']
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=theme_colors['foreground'],
            background=theme_colors['background'],
            padding=0,
            scale=0.9
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=theme_colors['foreground'],
            background=theme_colors['background']
        ),
        widget.Sep(
            linewidth=2,
            padding=6,
            size_percent=60,
            foreground=theme_colors['color8'],
            background=theme_colors['background']
        ),
        widget.TaskList(
            background=theme_colors['background'],
            border=theme_colors['color4'],
            borderwidth=2,
            font=fontconfig['text']+' Medium',
            fontsize=12,
            foreground=theme_colors['foreground'],
            highlight_method="block",
            icon_size=0,
            margin=3,
            markup=True,
            markup_focused='<span color="'+theme_colors['background']+'">{}</span>',
            padding=6,
            rounded=True,
            spacing=2,
            txt_floating='',
            txt_maximized='',
            txt_minimized='',
            urgent_alert_method='border',
            urgent_border=theme_colors['color1'],
            unfocused_border=theme_colors['color8']
        ),
        widget.Spacer(
            background=theme_colors['background']
        ),
        widget.Systray(
            background=theme_colors['background'],
            icon_size=18,
            padding=12
        ),
        widget.Sep(
            linewidth=0,
            padding=8,
            foreground=theme_colors['foreground'],
            background=theme_colors['background'],
        ),
        widget.Sep(
            linewidth=2,
            padding=6,
            size_percent=60,
            foreground=theme_colors['color8'],
            background=theme_colors['background'],
        ),
        widget.Clock(
            foreground=theme_colors['foreground'],
            background=theme_colors['background'],
            font=fontconfig['text'],
            fontsize=14,
            padding=10,
            format="%B %_d{}, %H:%M".format(day_suffix()),
            mouse_callbacks={'Button1': toggle_eww_calendar}
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=theme_colors['foreground'],
            background=theme_colors['background']
        )
    ]
    return widgets_list

# No bar config
# def init_screens():
#     return [Screen()]

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets(),
                               opacity=1.0,
                               size=dpi(32),
                               margin=0),
                   # bottom=bar.Bar([],
                   #                size=dpi(66),
                   #                opacity=0.0,
                   #                margin=0),
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

floating_layout_theme = layout_theme.copy()
floating_layout_theme.update({ "border_width": 0 })

##### FLOATING WINDOWS #####
floating_layout = layout.Floating(
    **floating_layout_theme,
    float_rules=[
        *layout.Floating.default_float_rules,
        # default_float_rules include: utility, notification, toolbar, splash, dialog,
        # file_progress, confirm, download and error.
        # Match(wm_type="utility"),
        # Match(wm_type="notification"),
        # Match(wm_type="toolbar"),
        # Match(wm_type="splash"),
        # Match(wm_type="dialog"),
        # Match(wm_class="confirm"),
        # Match(wm_class="dialog"),
        # Match(wm_class="download"),
        # Match(wm_class="error"),
        # Match(wm_class="file_progress"),
        # Match(wm_class="notification"),
        # Match(wm_class="splash"),
        # Match(wm_class="toolbar"),
        # Match(wm_class="confirmreset"),  # gitk
        # Match(wm_class="makebranch"),  # gitk
        # Match(wm_class="maketag"),  # gitk
        # Match(title="branchdialog"),  # gitk
        # Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="ssh-askpass"),  # ssh-askpass
        # Match(wm_class="thunar"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="sxiv"),
        Match(wm_class="feh"),
        # Match(wm_class="galculator"),
        # Match(wm_class="blueman-manager"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "smart"

##### HOOKS #####
# @hook.subscribe.layout_change
# def disable_rcorners(qtile):
#     c.screen.info()['`

##### STARTUP APPLICATIONS #####

@hook.subscribe.startup_once
def start_once():
    command=[ os.path.expanduser('~/.config/qtile/autostart.sh') ]
    subprocess.call(command)

@hook.subscribe.restart
def on_restart():
    command=[ os.path.expanduser('~/.config/qtile/icons.sh'), theme_colors['color4'] ]
    subprocess.call(command)

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
