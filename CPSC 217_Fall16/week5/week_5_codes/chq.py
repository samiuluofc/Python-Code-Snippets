from SimpleGraphics import *

for col in range(0, 8): 
    for row in range (0, 6):
        # Computer x and y for the top-left corner of the square
        x = col * 100
        y = row * 100
        # if it is a black square (row and column are both even or odd)
        if ((row % 2) == (col % 2)):
            setFill("black")
        else:
            setFill("white")
        rect(x, y, 100, 100)
