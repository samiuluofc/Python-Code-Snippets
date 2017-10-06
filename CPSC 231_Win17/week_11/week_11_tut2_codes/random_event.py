# basic moving box

import engine
import turtle
import random

WIDTH = 640
HEIGHT = 480

class Box(engine.GameObject):
	def __init__(self,xcor):
		super().__init__(xcor,240, 0, -2, 'square', 'red')

class Circle(engine.GameObject):
	def __init__(self,ycor):
		super().__init__(320, ycor, -2, 0, 'circle', 'blue')


def add_circle():
        ycor = random.randint(-240,+240)
        engine.add_obj(Circle(ycor))

def add_box():
        xcor = random.randint(-320,+320)
        engine.add_obj(Box(xcor))
	

if __name__ == '__main__':
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	
	engine.add_random_event(0.02,add_circle)
	engine.add_random_event(0.02,add_box)
	
	engine.engine()
