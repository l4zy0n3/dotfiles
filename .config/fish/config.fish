set SPACEFISH_CHAR_PREFIX '🔥🔥🔥 '
# Load aliases and shortcuts if existent.
alias shut "sudo shutdown now"
alias cp "cp -iv"
alias mv "mv -iv"
alias rm "rm -vI"
alias cdir "mkdir -pv"
alias dl "aria2c -x16"
alias yt "youtube-dl --add-metadata -i"
alias yta "yt -x -f bestaudio/best"
alias ffmpeg "ffmpeg -hide_banner"
#alias vim "kak"
alias dmen 'dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'
alias startjenkins 'docker run -d -v /home/yt/jenkins:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts'
alias memtop 'ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head'
alias cputop 'ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head'
alias gdrive 'google-drive-ocamlfuse /home/yt/GoogleDrive/'
alias add 'git add'
alias commit 'git commit -m '
alias push 'git push'

#function fish_greeting
#	cowfortune -a
#end

#funcsave fish_greeting
command wal -R -q
command cat ~/.cache/wal/sequences &

function kak
    /usr/bin/kak "$argv[1]"
    wal -Rneq
end

function apply-wall-dark
   command wal --saturate="$argv[3]" -n -i "$argv[1]" --backend "$argv[2]"
   command feh --bg-scale "$argv[1]"
   command betterlockscreen -u "$argv[1]"
   command reTheme "$argv[1]"
end

function apply-wall-light
   command wal -l --saturate="$argv[3]" -n -i "$argv[1]" --backend "$argv[2]"
   command feh --bg-scale "$argv[1]"
   command betterlockscreen -u "$argv[1]"
   command reTheme "$argv[1]"
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
