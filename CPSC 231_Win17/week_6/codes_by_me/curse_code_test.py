'''
The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals
'''

import curses
import time

stdscr = curses.initscr()


curses.noecho()

#stdscr.echo()
#stdscr.nocbreak()
#stdscr.keypad(0)

stdscr.addstr(0,0, "RED ALERT!")
stdscr.refresh()
time.sleep(1)


ch = stdscr.getkey()
stdscr.addstr(10,10, ch)
stdscr.refresh()
time.sleep(10)
