# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile.config import ScratchPad, DropDown, Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import extension,layout, bar, widget, hook
from typing import List  # noqa: F401
from colors import special, colors
#minimal = False
minimal = True
#colors = shuffled

def backlight(action):
    def f(qtile):
        brightness = int(float(str(subprocess.run(['xbacklight', '-get'], stdout=subprocess.PIPE).stdout)[2:-4]))
        if ((brightness == 100 and action == 'inc' ) or (brightness == 1 and action == 'dec' )):
            pass
        else:
            if brightness != 1 or action != 'dec':
                if (brightness > 49 and action == 'dec') \
                                    or (brightness > 39 and action == 'inc'):
                    subprocess.run(['xbacklight', f'-{action}', '10'])
                elif (brightness > 49 or (brightness < 39 and brightness > 25)):
                    subprocess.run(['xbacklight', f'-{action}', '5'])
                else:
                    subprocess.run(['xbacklight', f'-{action}', '1'])
    return f

def get_text_color(hex_str):
    hex_str = hex_str[1:]
    (r, g, b) = (hex_str[:2], hex_str[2:4], hex_str[4:])
    return colors[-1] if 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255 < 0.5 else '#ffffff'


mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
myConfig = "/home/yt/.config/qtile/config.py"    # The Qtile config file location
myEditor = "kak"
keys = [
	Key([mod], "v", lazy.spawn(myTerm + " -e cava")),
	Key([mod], "y", lazy.screen.prev_group()),
	Key([mod], "u", lazy.screen.next_group()),
	Key([mod, "shift"], "Left", lazy.screen.prev_group()),
	Key([mod, "shift"], "Right", lazy.screen.next_group()),
	Key([mod], "comma", lazy.spawn("rofimoji")),
	Key([mod], "d", lazy.spawn("rofi -combi-modi window,run -show combi -modi combi")),
	Key([mod], "period", lazy.group["SPD"].dropdown_toggle("terminal")),
	Key([mod], "p", lazy.group["SPD"].dropdown_toggle("python")),
	Key([mod], "o", lazy.group["SPD"].dropdown_toggle("ranger")),
        Key([mod, "shift"], 'e', lazy.spawn(myTerm + ' -e ' + myEditor + ' ' + myConfig)),
        Key([], 'F7', lazy.spawn('xset dpms force off')),
        Key([], 'XF86MonBrightnessUp',   lazy.function(backlight('inc'))),
        Key([], 'XF86MonBrightnessDown', lazy.function(backlight('dec'))),
        Key([], 'XF86AudioMute', lazy.spawn('ponymix toggle')),
        Key([], 'XF86AudioRaiseVolume', lazy.spawn('ponymix --max-volume 150 increase 5')),
        Key([], 'XF86AudioLowerVolume', lazy.spawn('ponymix decrease 5')),
        Key([mod], "Return",
             lazy.spawn(myTerm + " -e fish"),
             desc='Launches My Terminal'
             ),
        Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "x",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod, "shift"], "l",
             lazy.spawn('betterlockscreen -s dimblur'),
             desc='Suspend Qtile'
             ),
        Key([mod], "w",
             lazy.spawn("firefox"),
             desc='Firefox'
             ),
         Key([mod], "z",
             lazy.hide_show_bar("top")
             ),
         ### Treetab controls
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([], "F11",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
	Key([mod], "F11",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         Key([mod ], "a",
             lazy.spawn(myTerm+" -e pulsemixer"),
             desc='pulsemixer'
             ),
	Key([mod ], "s",
             lazy.spawn("spotify"),
             desc='spotify'
             ),
         Key([mod, "shift"], "h",
	     lazy.spawn(myTerm+" -e htop"),
             desc='Run HTOP'
             ),
]

group_names = [
	       ("\ue795", {'layout': 'monadtall'}),
               ("\uf269", {'layout': 'monadtall'}),
               ("\ufb0f", {'layout': 'monadtall'}),
               ("\uf1bc", {'layout': 'monadtall'}),
               ("\uf7c9", {'layout': 'monadtall'}),
               ("\uf308", {'layout': 'monadtall'}),
               ("\uf719", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
groups.append(
        ScratchPad("SPD",
            dropdowns = [
                DropDown("terminal",\
                        myTerm+" -e fish",\
                        y = 0.151,\
                        height = 0.75,\
                        opacity = 1.0,\
                        warp_pointer=False),
                DropDown("python",\
                        myTerm+" -e python",\
                        y = 0.151,\
                        height = 0.75,\
                        opacity = 1.0,\
                        warp_pointer=False),
                DropDown("ranger",\
                        myTerm+" -e ranger",\
                        y = 0.151,\
                        height = 0.75,\
                        opacity = 1.0,\
                        warp_pointer=False),
                ]
            )
        )
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {
                "border_width": 0,
                "margin": 10,
                "border_focus": special["foreground"],
                "border_normal": special["background"]
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "FantasqueSansMono Nerd Font",
         fontsize = 13,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 12,
         bg_color = special["background"][1:],
         active_bg = colors[0][1:],
         active_fg = colors[1][1:],
         inactive_bg = colors[-1][1:],
         inactive_fg = colors[-2][1:],
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
    layout.Floating(**layout_theme)
]
'''
colors = [["#292d3e", "#292d3e"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name
'''



prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
#    font="San Francisco Pro",
    font="FantasqueSansMono Nerd Font",
    fontsize = 18,
    padding = 6,
    background=special["background"],
    foreground=special["foreground"]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
    	      widget.Clock(
                       foreground = get_text_color(colors[6]),
                       background = colors[6],
                       format = " %H:%M ",
                       #fontsize = 16
                       ),
              widget.TextBox(
                       text = u'\ue0c6',
                       foreground = colors[6],
                       fontsize = 32,
                       padding=0
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2]
                       ),
              widget.GroupBox(
                       font = "Caskaydia Cove Nerd Font Mono",
                       fontsize = 30,
                       margin_y = 3,
                       margin_x = 3,
                       padding_y = 6,
                       padding_x = 6,
                       borderwidth = 3,
                       active = colors[5],
                       inactive = colors[6],
                       rounded = False,
                       highlight_color = colors[-1],
                       highlight_method = "line",
                       this_current_screen_border = colors[3],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[-3],
                       other_screen_border = colors[-3],
                       foreground = colors[-1],
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Caskaydia Cove Nerd Font Mono",
                       padding = 10,
                       foreground = colors[3],
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       ),
              widget.Sep(
                       linewidth = 0,
                       foreground = colors[2],
                       ),
	      widget.TextBox(
                       text = u'\ue0c7',
                       #text = u'\ue0c2',
		       fontsize = 32,
		       foreground = colors[1],
		       padding=2
                       ),
              widget.TextBox(
                       text = 'ﮮ' if minimal else '🌀',
                       background = colors[1],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e yay -Syu')},
                       fontsize = 20,
		       foreground = get_text_color(colors[1])
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       #custom_command = 'sudo pacman -Qu',
                       colour_have_updates = get_text_color(colors[0]),
                       colour_no_updates = get_text_color(colors[2]),
                       display_format = '{updates} Updates',
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e yay -Syu')},
                       background = colors[2],
                       foreground = get_text_color(colors[2])
                       ),
              widget.TextBox(
                       text = u'\ue0c7',
                       foreground = colors[2],
                       background = colors[1],
                       fontsize = 32,
                       padding=0
                       ),
              widget.Volume(
                       emoji= False if minimal else True,
                       foreground = get_text_color(colors[2]),
                       background = colors[2],
                       padding = 5,
                       volume_up_command = 'ponymix --max-volume 150 increase 5',
                       volume_down_command = 'ponymix decrease 5',
		       fontsize = 24
	              ),
             #widget.Volume(
             #          foreground = get_text_color(colors[2]),
             #          background = colors[2],
             #          padding = 5,
             #         ),
	     widget.TextBox(
                       text = u'\ue0c7',
                       foreground = colors[3],
                       background = colors[2],
                       fontsize = 32,
                       padding=0
                       ),
             widget.Battery(
                       format='{char}{percent:2.0%} {hour:d}:{min:02d}',
                       charge_char= u"\uf58a " if minimal else "🔌",
                       discharge_char= u"\uf578 " if minimal else "🔋",
                       full_char= u"\uf58b " if minimal else "👌",
                       empty_char=u"\uf582 " if minimal else "❌",
                       update_interval = 30,
                       foreground = get_text_color(colors[3]),
                       background = colors[3],
                       fontsize = 20
		       ),
              widget.TextBox(
                       text = "\ue0c7",
                       foreground = colors[4],
                       background = colors[3],
                       fontsize = 32,
                       padding=0
                       ),
	      widget.TextBox(
                        text=u"\uf85a " if minimal else "👾",
                        foreground = get_text_color(colors[4]),
                        background = colors[4],
                        fontsize = 20
                      ),
              widget.Memory(
                       foreground = get_text_color(colors[4]),
                       background = colors[4],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
	      widget.TextBox(
                       text = "\ue0c7",
                       foreground = colors[5],
                       background = colors[4],
                       fontsize = 32,
                       padding=0
                       ),
	      #widget.Systray(
              #         background = colors[1],
              #         padding = 5
              #         ),
              widget.TextBox(
                       text = u'\ufaa8 ',
                       foreground = get_text_color(colors[5]),
                       fontsize = 24,
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e nmtui-connect')},
                       ),
	      widget.Wlan(
			format =  "{essid} " + "{percent:2.0%}",
    			interface="wlp2s0",
                        foreground = get_text_color(colors[5]),
                        background = colors[5],
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e nmtui-connect')},
                       ),
              widget.TextBox(
                       text = u'\uf293',
                       foreground = get_text_color(colors[5]),
                       fontsize = 24,
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('blueman-manager')},
                       ),
              #widget.Wlan(
              #          interface="wlp2s0",
              #          background = colors[1],
              #          mouse_callbacks = {'Button1': lambda qtile: lazy.spawn(myTerm + ' -e nmtui-connect')},
              #        ),
              widget.TextBox(
                       text = u'\ue0c7',
                       foreground = colors[6],
                       background = colors[5],
                       fontsize = 32,
                       padding=0
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[6],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.Clock(
                       foreground = get_text_color(colors[6]),
                       background = colors[6],
                       #fontsize = 16,
                       format = "%A, %B %d "
                       )
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), margin=[8, 8, 5, 8],opacity=0.80, size=36)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=26)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=26))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod, 'shift'], "Button1", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod, "mod1"], "Button1", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

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
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

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
wmname = "LG3D"
