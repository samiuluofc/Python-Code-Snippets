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
screen.addshape('rock.gif')
screen.addshape('boom.gif')
		
class boom(engine.GameObject):
	def __init__(self,xcor,ycor):
		super().__init__(xcor,ycor, -2, -2, 'turtle', 'green')

	def draw(self):
		turtle.goto(self.x, self.y)
		turtle.shape("boom.gif")
		return turtle.stamp()

	def getxy(self):
		return self.x, self.y

class rock(engine.GameObject):
	def __init__(self,xcor):
		super().__init__(xcor,240, 0, -2, 'turtle', 'green')
		
	def draw(self):
		turtle.goto(self.x, self.y)
		turtle.shape("rock.gif")
		return turtle.stamp()
	
	def getxy(self):
		return self.x, self.y

class truck(engine.GameObject):
	def __init__(self,ycor):
		super().__init__(-320, ycor, 2, 0, 'turtle', 'blue')
		                
	def draw(self):
		turtle.goto(self.x, self.y)
		turtle.shape("truck.gif")
		return turtle.stamp()
		
	def getxy(self):
		return self.x, self.y

		
def effect(b,t):
        x1,y1 = b.getxy()
        x2,y2 = t.getxy()
        xcor = (x1+x2)/2
        ycor = (y1+y2)/2

        if abs(x1 - x2) < 40 and abs(y1 - y2) < 40:
                engine.add_obj(boom(xcor,ycor))
                engine.del_obj(b)
                engine.del_obj(t)
     

def add_truck():
        ycor = random.randint(-240,+240)
        engine.add_obj(truck(ycor))

def add_rock():
        xcor = random.randint(-320,+320)
        engine.add_obj(rock(xcor))

	

if __name__ == '__main__':
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	
	engine.add_random_event(0.02,add_truck)
	engine.add_random_event(0.02,add_rock)

	engine.register_collision(rock, truck, effect)
	engine.register_collision(truck, rock, effect)
	
	
	engine.engine()
