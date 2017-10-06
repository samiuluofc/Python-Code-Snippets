## Test the shapes available in the SimpleGraphics module.  When this program
#  runs it should display:
#
#    A gray circle with a black outline,
#    A cyan rectangle with a red outline,
#    A tomato colored curve
#    A blue line with 3 segments,
#    The text "Hello World!" in green,
#    A flesh colored blob with a purple outline
#    A pruple three-quarters arc,
#    A pink polygon with gray outline.
#    A yellow pie slice with orange outline, and
#
#  The name of each shape should appear below it in small black text.
#
from SimpleGraphics import *

# Change the window size and background color
resize(800, 700)
background("white")

# Draw the ellipse
setFill("gray75")
ellipse(100, 100, 100, 100)

# Draw the rectangle
setOutline("red")
setFill("light cyan")
rect(300, 100, 200, 100)

# Draw the line segments
setOutline("blue")
line(150, 350, 200, 400)
line(100, 400, 100, 300, 200, 300, 200, 350)

# Draw the text
setOutline("darkgreen")
setFont("Times", "24", "bold")
text(400, 350, "Hello World!", "c")

# Draw the arc
setOutline("purple")
arc(100, 500, 100, 100, 0, 270)

# Draw the pie slice
setOutline("Orange")
setFill("yellow")
pieSlice(600, 500, 100, 100, 60, 60)

# Draw the polygon
setOutline("gray50")
setFill("pink")
polygon(300, 500, 350, 500, 500, 550, 500, 600, 450, 600, 300, 550)

# Draw a curve
setOutline("tomato")
curve(600, 125, 600, 100, 700, 100, 700, 125, 600, 150, 600, 200, 700, 200, 700, 150)

# Draw a blob
setOutline("dark orchid")
setFill("bisque")
blob(600, 400, 600, 350, 700, 350, 700, 300, 650, 300, 650, 400)

# Label all of the shapes
setOutline("Black")
setFont("Arial", 10)
text(150, 225, "ellipse")
text(400, 225, "rect")
text(650, 225, "curve")
text(150, 425, "line")
text(400, 425, "text")
text(650, 425, "blob")
text(150, 625, "arc")
text(650, 625, "pieSlice")
text(400, 625, "polygon")
