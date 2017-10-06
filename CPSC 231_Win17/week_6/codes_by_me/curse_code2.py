'''
The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals
'''

import curses
import time

stdscr = curses.initscr()

#curses.noecho()

stdscr.addstr(0,0, "RED ALERT!")
stdscr.refresh()
time.sleep(1)

stdscr.addch(1,0, 'A')
stdscr.refresh()
time.sleep(1)

ch = stdscr.getkey()
ch = stdscr.getkey()

stdscr.move(0,10)
stdscr.deleteln()

ch = stdscr.inch(0,1)
stdscr.addch(10,10, ch)

ch = stdscr.getkey()




