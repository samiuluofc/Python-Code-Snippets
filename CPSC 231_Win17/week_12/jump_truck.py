# basic moving box

import engine
import turtle
import random

WIDTH = 640
HEIGHT = 480

turtle.bgcolor('black')
turtle.tracer(1000)
screen = turtle.Screen()
screen.addshape('truck.gif')



		
class truck(engine.GameObject):
	def __init__(self,xcor,ycor):
		super().__init__(xcor, ycor, 0, 0, 'turtle', 'blue')
		self.count = 0
		
	def draw(self):
		turtle.goto(self.x, self.y)
		turtle.shape("truck.gif")
		return turtle.stamp()

	def move(self):

		if self.deltay == 1:
			self.y = self.y + self.deltay
			self.count = self.count + 1

		if self.deltay == -1:
			self.y = self.y + self.deltay
			self.count = self.count - 1

		if self.count == 60:
			self.deltay = -1

		if self.deltay == -1 and self.count == 0:
			self.deltay = 0
	
	def getxy(self):
		return self.x, self.y

truck_obj = truck(0,0)

def jump(key):
        if key == 'space':
                if truck_obj.deltay == 0:
                        truck_obj.deltay = 1


if __name__ == '__main__':
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	engine.add_obj(truck_obj)
	engine.set_keyboard_handler(jump)
	engine.engine()
