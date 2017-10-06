import config
import curses
import time

scr = curses.initscr()
curses.noecho()

#print(config.CONFIG)
MAPROWS = 22
MAPCOLS = 80
MAPWALL = '.'

my_map = []
for i in range(MAPROWS):
    my_map.append([MAPWALL] * MAPCOLS)


lines = config.CONFIG.split("\n")

# Parsing room info
room_list = []
for each_line in lines:
    if each_line[0:4] == 'room':

        word_list = each_line.split(' ')
        ulx = int(word_list[1])
        uly = int(word_list[2])
        w = int(word_list[3])
        h = int(word_list[4])

        label = ''
        for i in range(5,len(word_list)):
            label = label + word_list[i] + ' '
            
        room_list.append([ulx, uly, w, h, label])

#Parsing char info
char_list = []
for each_line in lines:
    if each_line[0:4] == 'char':

        word_list = each_line.split(' ')
        ch = word_list[1]
        chx = int(word_list[2])
        chy = int(word_list[3])

        char_list.append([ch, chx, chy])

# Plotting rooms in the map 
for room_info in room_list:

    [ulx, uly, w, h, label] = room_info

    for i in range(uly,uly+h):
        for j in range(ulx,ulx+w):
            my_map[i][j] = ' '

# Plotting chars in the map
for char_info in char_list:
    [ch, chx,  chy] = char_info
    my_map[chy][chx] = ch

# Printing the map
map_str = ''
for i in range(MAPROWS):
    for j in range(MAPCOLS):
        map_str = map_str + my_map[i][j]
    #map_str = map_str + '\n'

#print(map_str)

# Working on curses module

scr.addstr(0,0,map_str)
scr.refresh()

curx = room_list[0][0]
cury = room_list[0][1]
x = curx
y = cury
lastx = curx
lasty = cury

while True:

    # For making room message
    for r in range(len(room_list)-1,-1,-1):
        [ulx, uly, w, h, label] = room_list[r]
        if curx >= ulx and curx < ulx + w and cury >= uly and cury < uly + h:
            scr.addstr(23,10, ' ' * 70)
            scr.addstr(23,10,label)
            scr.move(cury,curx)

    # Add the game person
    scr.addch(lasty,lastx,my_map[lasty][lastx])
    scr.addch(cury,curx,'@')
    scr.refresh()

    # Taking input and process it
    ch = scr.getkey()
    
    
    if(ch == 'i'):
        y = cury - 1
        x = curx
        
    if(ch == 'k'):
        y = cury + 1
        x = curx
        
    if(ch == 'j'):
        x = curx - 1
        y = cury
        
    if(ch == 'l'):
        x = curx + 1
        y = cury

    # Checking boundary
    if (y >=0 and y < MAPROWS and x >= 0 and x < MAPCOLS):
        if (my_map[y][x] != '.'):
            lastx = curx
            lasty = cury
            curx = x
            cury = y
            

            
