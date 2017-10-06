# basic moving box

import engine
import turtle
import random

score = 0
turtle.bgcolor('cyan')
turtle.tracer(1000)
turtle.goto(0,0)

def draw_score():
        turtle.goto(-35,45)
        turtle.fillcolor('cyan')
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()
        turtle.goto(0,0)
        turtle.color('black')
        turtle.write(str(score), align='center', font=('Arial', 25, 'normal'))


WIDTH = 640
HEIGHT = 480

class Box(engine.GameObject):
	def __init__(self,xcor):
		super().__init__(xcor,240, 0, -2, 'square', 'red')

	def getxy(self):
		return self.x, self.y
        
class Triangle(engine.GameObject):
	def __init__(self,ycor):
		super().__init__(320, ycor, -2, 0, 'triangle', 'blue')
		
	def getxy(self):
		return self.x, self.y
        
class Circle(engine.GameObject):
	def __init__(self,xcor,ycor):
		super().__init__(xcor, ycor, -2, -2, 'circle', 'yellow')


		
def effect(b,t):
        x1,y1 = b.getxy()
        x2,y2 = t.getxy()
        xcor = (x1+x2)/2
        ycor = (y1+y2)/2

        if abs(x1 - x2) < 20 and abs(y1 - y2) < 20:
                engine.add_obj(Circle(xcor,ycor))
                engine.del_obj(b)
                engine.del_obj(t)
                global score
                score = score + 1
                draw_score()

def add_tri():
        ycor = random.randint(-240,+240)
        engine.add_obj(Triangle(ycor))

def add_box():
        xcor = random.randint(-320,+320)
        engine.add_obj(Box(xcor))
	

if __name__ == '__main__':
	engine.init_screen(WIDTH, HEIGHT)
	engine.init_engine()
	
	engine.add_random_event(0.1,add_tri)
	engine.add_random_event(0.1,add_box)

	engine.register_collision(Box, Triangle, effect)
	engine.register_collision(Triangle, Box, effect)
	
	engine.engine()
