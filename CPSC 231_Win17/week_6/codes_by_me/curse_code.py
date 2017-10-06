'''
The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals
'''

import curses
import time

stdscr = curses.initscr()

curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_RED)

curses.noecho()
curses.cbreak()
stdscr.keypad(1)

#stdscr.echo()
#stdscr.nocbreak()
#stdscr.keypad(0)

win.addstr(0,0, "RED ALERT!")
time.sleep(1)
win.refresh()

stdscr.addstr(1,0, "RED ALERT!", curses.A_REVERSE)
time.sleep(1)
stdscr.refresh()

stdscr.addstr(2,0, "RED ALERT!", curses.A_DIM)
time.sleep(1)
stdscr.refresh()

stdscr.addstr(3,0, "RED ALERT!", curses.color_pair(1))
time.sleep(1)
stdscr.refresh()	

ch = stdscr.getch()