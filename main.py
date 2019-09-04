import pygame 
import os 
os.environ['SDL_VIDEO_CENTERED'] = '1'

from pygame.locals import *

#Helper class that controls interaction loop in Pygame
from pygamehelper import *

#Get the definition of the World
from BugWorld import *

#main control loop of the pygame
class BugSim( PygameHelper ):
	
	def __init__(self):
		self.BW = BugWorld()  # instantiate the world and its objects
		super(BugSim, self).__init__((self.BW.BOUNDARY_WIDTH, self.BW.BOUNDARY_HEIGHT), Color.WHITE)
		self.pause = False
		self.draw_screen = True

	def update(self):  # update everything in the world
		if self.BW.exit_simulation:
			self.running = False
		elif not self.pause:
			self.BW.update()

	def draw(self):  # draw the resulting world
		if self.draw_screen:
			self.screen.fill(Color.WHITE)
			self.BW.draw(self.screen)
			pygame.display.update()

	def keyDown(self, key):
		
		if key == K_SPACE:  # pause the game
			if self.pause:
				self.pause = False
			else:
				self.pause = True

		if key == K_d:  # pause the game
			if self.draw_screen:
				self.draw_screen = False
			else:
				self.draw_screen = True

		elif key == K_LEFT:
			pass
		elif key == K_RIGHT:
			pass
		else:
			print(key)

	def keyUp(self, key):
		pass

	def mouseUp(self, pos):
		pass

	def mouseUp2(self, pos):
		pass


if __name__ == "__main__":
	g = BugSim()
	g.mainLoop(60)
'''

https://docs.python.org/3/library/argparse.html

https://stackoverflow.com/questions/39390418/python-how-can-i-enable-use-of-kwargs-when-calling-from-command-line-perhaps
def f(log=None, bin=None, pid=None, conf=None):
    self.log = log
    self.bin = bin
    self.pid = pid
    self.conf = conf
'''