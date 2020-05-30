# My Qtile Configuration

![Screenshot of my desktop](https://www.gitlab.com/dwt1/dotfiles/raw/master/.screenshots/dotfiles07.png)

A full-featured, pure-Python tiling window manager

# Features

* Simple, small and extensible. It's easy to write your own layouts,
  widgets and commands.
* Configured in Python.
* Command shell that allows all aspects of Qtile to be managed and
  inspected.
* Complete remote scriptability - write scripts to set up workspaces,
  manipulate windows, update status bar widgets and more.
* Qtile's remote scriptability makes it one of the most thoroughly
  unit-tested window managers around.

# My Keybindings

The MODKEY is set to the Super key (aka the Windows key).  I try to keep the
keybindings consistent with all of my window managers.

| Keybinding | Action |
| :--- | :--- |
| `MODKEY + RETURN` | opens terminal (alacritty is the terminal but can be easily changed) |
| `MODKEY + SHIFT + RETURN` | opens run launcher (dmenu is the run launcher but can be easily changed) |
| `MODKEY + TAB` | rotates through the available layouts |
| `MODKEY + SHIFT + c` | closes window with focus |
| `MODKEY + SHIFT + r` | restarts qtile |
| `MODKEY + SHIFT + q` | quits qtile |
| `MODKEY + 1-9` | switch focus to workspace (1-9) |
| `MODKEY + SHIFT + 1-9` | send focused window to workspace (1-9) |
| `MODKEY + j` | lazy layout up (switches focus between windows in the stack) |
| `MODKEY + k` | lazy layout down (switches focus between windows in the stack) |
| `MODKEY + SHIFT + j` | lazy layout shuffle_up (rotates the windows in the stack) |
| `MODKEY + SHIFT + k` | lazy layout shuffle_down (rotates the windows in the stack) |
| `MODKEY + h` | expand size of window (MondadTall layout) |
| `MODKEY + l` | shrink size of window (MondadTall layout) |
| `MODKEY + w` | switch focus to monitor 1 |
| `MODKEY + e` | switch focus to monitor 2 |
| `MODKEY + r` | switch focus to monitor 3 |
| `MODKEY + period` | switch focus to next monitor |
| `MODKEY + comma` | switch focus to prev monitor |

# Community

Qtile is supported by a dedicated group of users. If you need any help, please
don't hesitate to fire off an email to our mailing list or join us on IRC.

* Mailing List: http://groups.google.com/group/qtile-dev
* IRC: irc://irc.oftc.net:6667/qtile

