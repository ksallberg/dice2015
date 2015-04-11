import pygame
import os.path
from pygame.locals import *
from terrain import Terrain

class Main():

	sprites = {}
	myMissiles = []
	enemyMissiles = []
	clock	= None
	screen	= None
	planePosition = [100,150]
	deltaMovement = 2
	terrain = None

	def __init__(self):
		print "hello"
		pygame.init()

		pygame.display.set_caption('Wallstreet Tycoon')

		self.terrain = Terrain()
		self.screen = pygame.display.set_mode((800,400))
		self.clock = pygame.time.Clock()
		self.sprites["plane"] = pygame.image.load(os.path.join('sprites','plane.png'))
		self.sprites["missile"] = pygame.image.load(os.path.join('sprites','missile.png'))

	def main_loop(self):
		while True:
			self.screen.fill((0,0,0))
			self.clock.tick(60)
			
			keys = pygame.key.get_pressed()
			if keys[K_UP]:
				self.planePosition[1] = self.planePosition[1] - self.deltaMovement;
			if keys[K_DOWN]:
				self.planePosition[1] = self.planePosition[1] + self.deltaMovement;
			if keys[K_SPACE]:
				self.myMissiles.append([self.planePosition[0] + self.sprites["missile"].get_width(), self.planePosition[1]])
			
			for e in pygame.event.get():
				continue
			
			self.drawSprites()
			
			self.terrain.draw(self.screen)
			pygame.display.flip()
	
	def drawSprites(self):
		self.screen.blit(self.sprites["plane"], self.planePosition)
		for missile in self.myMissiles:
			self.screen.blit(self.sprites["missile"], missile)

	
if __name__ == '__main__':
	main = Main()
	main.main_loop()
