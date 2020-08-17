set SPACEFISH_CHAR_PREFIX '🔥🔥🔥 '
# Load aliases and shortcuts if existent.
alias shut "sudo openrc-shutdown -p now"
alias cp "cp -iv"
alias mv "mv -iv"
alias rm "rm -vI"
alias cdir "mkdir -pv"
alias dl "aria2c -x16"
alias yt "youtube-dl --add-metadata -i"
alias yta "yt -x -f bestaudio/best"
alias ffmpeg "ffmpeg -hide_banner"
alias vim "kak"
alias dmen 'dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'

#function fish_greeting
#	cowfortune -a
#end

#funcsave fish_greeting
command wal -R -q
command cat ~/.cache/wal/sequences &
function apply-wall-dark
   command wal --saturate="$argv[3]" -n -i "$argv[1]" --backend "$argv[2]"
   command feh --bg-scale "$argv[1]"
   command betterlockscreen -u "$argv[1]"
end

function apply-wall-light
   command wal -l --saturate="$argv[3]" -n -i "$argv[1]" --backend "$argv[2]"
   command feh --bg-scale "$argv[1]"
   command betterlockscreen -u "$argv[1]"
end

function mkdir -d "Create a directory and set CWD"
    command mkdir $argv
    if test $status = 0
        switch $argv[(count $argv)]
            case '-*'

            case '*'
                cd $argv[(count $argv)]
                return
        end
    end
end
# [ -f "$XDG_CONFIG_HOME:-$HOME/.config/shortcutrc" ] && source "$XDG_CONFIG_HOME:-$HOME/.config/shortcutrc"
# [ -f "$XDG_CONFIG_HOME:-$HOME/.config/aliasrc" ] && source "$XDG_CONFIG_HOME:-$HOME/.config/aliasrc"
# [ -f "$XDG_CONFIG_HOME:-$HOME/.config/zshnameddirrc" ] && source "$XDG_CONFIG_HOME:-$HOME/.config/zshnameddirrc"
# set SPACEFISH_CHAR_SYMBOL '   '
