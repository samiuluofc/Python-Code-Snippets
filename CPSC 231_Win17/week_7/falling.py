# assumes 80x24 terminal window

import time
import curses
import random

COLS = 80
ROWS = 24

LONGDELAY = 2
DELAY = 0.01

# XXX would be better to use the predefined one in the string module
CHARS = 'abcdefghijklmnopqrstuvwxyz'

stdscr = curses.initscr()

while True:
	# use this to track where letters are - set up barrier on
	# bottom to make checking simpler in the code
	used = [ ]
	for i in range(ROWS):
		used.append( [False] * COLS )
	used.append( [True] * COLS )

	stdscr.clear()
	ci = 0

	while True:
		x = random.randint(0, COLS-1)
		oldy = 0
		y = 0

		# a letter's falling
		while not used[y][x]:
			stdscr.addch(oldy, x, ' ')
			stdscr.addch(y, x, CHARS[ci])
			oldy = y
			y = y + 1
			time.sleep(DELAY)
			stdscr.refresh()

		used[y-1][x] = True
		ci = (ci + 1) % len(CHARS)

		if True in used[0]:
			time.sleep(LONGDELAY)
			break
