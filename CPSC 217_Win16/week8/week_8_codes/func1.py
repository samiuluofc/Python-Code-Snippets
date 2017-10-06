from SimpleGraphics import *

"""
Definition: Draw a music note into a target location with desire color
@param x: x coordinate of the location
@param y: y coordinate of the location
@param color: Desire color name
"""
def music_note(x, y, color):
	setColor(color)		
	rect(0+x,0+y,100,10)
	rect(0+x,20+y,100,10)
	rect(0+x,0+y,10,100)
	ellipse(-30+x,90+y,40,30)
	rect(90+x,0+y,10,100)
	ellipse(60+x,90+y,40,30)

# Main function: Your program starts from here.
def main():
	background("white")
	music_note(50,100,"red")
	music_note(200,100,"black")
	music_note(350,100,"blue")
	music_note(500,100,"yellow")
	music_note(650,100,"green")

main()
