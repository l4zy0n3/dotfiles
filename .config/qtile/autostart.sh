#! /bin/dash 
#picom &
#nitrogen --restore &
#urxvtd -q -o -f &
cat ~/.cache/wal/sequences &
wal -q -R
albert &
picom --config=/home/yt/.config/picom/picom.conf --backend=glx &
