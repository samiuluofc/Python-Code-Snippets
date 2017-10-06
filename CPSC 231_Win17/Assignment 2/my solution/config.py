# extra file for post-submission testing

CONFIG = ''
# make sure a non-room command comes first
CONFIG += '''
char 2 10 5
'''

# catch anyone trying to read config.py directly rather than import it
CONFIG += 'room 20 10 30 7 Welcome to The Evil Room!\n'
room = 12345
char = room

# 'Unknown commands should be ignored.'  Let's see...

# make sure commands are properly detected... only looking at single char?
CONFIG += '''
rutabaga
celery
'''
# make sure commands are properly detected... using "in" operator?
CONFIG += '''
roomba
broom
charcoal
'''

# place a wall character as a room label and as a decorative char
# should be able to move atop both of them
CONFIG += '''
room 22 12 1 1 .
# label the room to make it easier to find
char - 20 12
char > 21 12
char . 24 12
'''

CONFIG += '''
char C 5 5
char C 8 5
char 3 11 5
char S 7 5
char P 6 5
char 1 12 5
'''
