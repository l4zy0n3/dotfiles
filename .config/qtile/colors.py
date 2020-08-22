'''
Input a string without hash sign of RGB hex digits to compute
complementary contrasting color such as for fonts
'''
import json
def lightness(hex_str):
    hex_str = hex_str[1:]
    (r, g, b) = (hex_str[:2], hex_str[2:4], hex_str[4:])
    return 1 - (int(r, 16) * 0.299 + int(g, 16) * 0.587 + int(b, 16) * 0.114) / 255
with open('/home/yt/.cache/wal/colors.json') as f:
    all_colors = json.load(f)

special = all_colors['special']
colors = set()
shuffled = []
for v in all_colors['colors'].values():
    colors.add( v)
    shuffled.append( v)
colors = list(colors)
colors.sort(key=lambda elem: lightness(elem))
'''
Sorts colors from light to dark
['#bfc4c7', '#a46c9f', '#5871ac', '#b13a6c', '#0b6baa', '#414f58', '#b51148', '#0d3aaa', '#021521']
'#c7c6c5', '#83a2a8', '#aa907b', '#70a4a6', '#6e92aa', '#607faa', '#4b69aa', '#585451', '#211c18'
'''
