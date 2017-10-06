# Sample Code: Created by SAMIUL AZAM, TA-217 (T-04)

from SimpleGraphics import *

# Change the window size and background color
resize(800, 500)
background("cyan")

# Here, x and y variables are used to place the object in the desire location 

x = 10
y = 30
setOutline("yellow")
setWidth("5")
setFill("green")
blob(0+x,0+y,200+x,0+y,200+x,200+y,0+x,200+y)


x = 250
y = 30
setOutline("green")
setWidth("5")
setFill("red")
blob(0+x,0+y,0+x,0+y, 200+x,0+y,200+x,200+y,200+x,200+y,0+x,200+y)

x = 420
y = 30
setOutline("white")
setWidth("5")
setFill("blue")
blob(0+x,0+y,400+x,0+y, 200+x,200+y,200+x,200+y)

x = 300
y = 300
setOutline("yellow")
setWidth("5")
curve(50+x,0+y, 100+x,0+y, 100+x,50+y, 150+x,50+y, 
150+x,100+y,100+x,100+y,100+x,150+y,50+x,150+y,50+x,
100+y,0+x,100+y,0+x,50+y,50+x,50+y,50+x,0+y)

x = 40
y = 300
setOutline("purple")
setWidth("5")
line(50+x,0+y, 100+x,0+y, 100+x,50+y, 150+x,50+y, 
150+x,100+y,100+x,100+y,100+x,150+y,50+x,150+y,50+x,
100+y,0+x,100+y,0+x,50+y,50+x,50+y,50+x,0+y)


x = 650
y = 300
setFont("Times", "24", "bold")
text(x, y, "Hello World!","c")

x = 550
y = 350
setOutline("black")
setWidth("2")
setFill("orange")
pieSlice(x,y,130,130,90,270)




