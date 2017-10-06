import time
import curses

ROWS = 24
COLS = 80
BORDERCHAR = '*'

# initialize curses
stdscr = curses.initscr()

# draw border
stdscr.addstr(0, 0, BORDERCHAR * COLS)
stdscr.addstr(ROWS-1, 0, BORDERCHAR * COLS)
for row in range(1, ROWS):
	stdscr.addch(row, 0, BORDERCHAR)
	stdscr.addch(row, COLS-1, BORDERCHAR)

# list of strings and their coordinates that we'll iterate through
# XXX not the best design, but works within the extent of what we've covered
L = [
	[ 5, 5, 'RED' ],
	[ 7, 5, 'YELLOW' ],
	[ 9, 5, 'GREEN' ],
]
i = 0

while True:
	# update string - erase old one (wraps thanks to negative indexing)
	last = L[i-1]
	stdscr.addstr(last[0], last[1], ' ' * len(last[2]))

	# update string - place new one
	next = L[i]
	stdscr.addstr(next[0], next[1], next[2])

	# update index
	i = (i + 1) % len(L)

	# won't see anything if this is forgotten!
	stdscr.refresh()

	# pause
	time.sleep(2)	

#would need this if the program exited to shut down curses cleanly

#curses.endwin()
