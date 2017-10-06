# Sample Code: Created by SAMIUL AZAM, TA-217 (T-04)

from SimpleGraphics import *

background("cyan")
setWidth("1")
setOutline("red")

it = 1
x = 100
y = 100

while it <= 10:

    if it % 2 == 0:
        setFill("green")
    else:
        setFill("white")

    ellipse(x,y,40,40)

    x = x + 40
    it = it + 1
