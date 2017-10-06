# Draw a simple scenario using python SimpleGraphics library
# Student ID: ********
# Name: xyz

# Importing simple graphics
from SimpleGraphics import *

# Set the background color
background("deep sky blue")

# Draw the cloud
setColor("white")
ellipse(30,35, 70, 70)
ellipse(60,35, 70, 70)
ellipse(100,50, 70, 70)
ellipse(140,35, 70, 70)
ellipse(180,40, 70, 70)
ellipse(195,55, 70, 70)
ellipse(180,75, 70, 70)
ellipse(125,75, 70, 70)
ellipse(85,77, 70, 70)
ellipse(50,78, 70, 70)

# Draw the sun
setColor("orange red")
pieSlice(652, -149, 300, 300, 180, 90)

# Draw the ground
setColor("lime green")
rect(0,400,900,200)

# Draw the house
setColor("azure4")
rect(240, 225, 409, 260)

# Draw the door
setColor("bisque2")
rect(265, 275, 100, 210)

# Draw the window
setColor("yellow")
setOutline("black")
rect(425,285,200,125)
setOutline("black")
rect(524.5,285,100,63)
rect(525,347.5,100,62.5)
rect(424.5,285,100,63)
rect(424.5,347.5,100,62.5)

# Draw the roof
setColor("dark olive green")
polygon(210,225,440,135,675,225,210,225)

# Draw the text
setColor("black")
setFont("Times", "14", "bold")
text(715, 585, "A simple house","c")

