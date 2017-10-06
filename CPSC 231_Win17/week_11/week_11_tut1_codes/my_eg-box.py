# basic moving box

import engine

WIDTH = 640
HEIGHT = 480

class shape(engine.GameObject):
	
	def move_left(self):
		self.x = self.x - 5
		self.update()
	def move_right(self):
		self.x = self.x + 5
		self.update()
	def move_up(self):
		self.y = self.y + 5
		self.update()
	def move_down(self):
		self.y = self.y - 5
		self.update()

	def dir_left(self):
		self.deltax = -1
		self.deltay = 0
		self.update()
			
	def dir_right(self):
		self.deltax = +1
		self.deltay = 0
		self.update()
		          
	def dir_up(self):
		self.deltay = +1
		self.deltax = 0
		self.update()
		
	def dir_down(self):
		self.deltay = -1
		self.deltax = 0
		self.update()

	def pause(self):
		print('Stop Auto Moving')
		self.deltay = 0
		self.deltax = 0
		self.update()


        #Overiding the delete function
	def delete(self):
		super().delete()# delete the object
		engine.exit_engine()
		print('Game Engine Exits')

def keyboard_cb(key):
	if key == 'a':
		s1.move_left()
	if key == 'd':
		s1.move_right()
	if key == 'w':
		s1.move_up()
	if key == 's':
		s1.move_down()

	if key == 'j':
		s1.dir_left()
	if key == 'l':
		s1.dir_right()
	if key == 'i':
		s1.dir_up()
	if key == 'k':
		s1.dir_down()

	if key == 'p':
		s1.pause()


		
engine.init_screen(WIDTH, HEIGHT)
engine.init_engine()

s1 = shape(40,40,0,0,'square','red')
s2 = shape(40,-40,0,0,'triangle','blue')
s3 = shape(0,0,0,0,'circle','green')

engine.add_obj(s1)
engine.add_obj(s2)
engine.add_obj(s3)

engine.set_keyboard_handler(keyboard_cb)

engine.engine()

	

# Automatically deletes all added objects from the game area when they
# go outside the defined screen size. But the engine is still running.
