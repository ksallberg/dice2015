import pygame
import os.path
from pygame.locals import *
from terrain import Terrain



class Plane():
	def __init__(self, sprite, initialPosition, deltaMovement):
		self.sprite = sprite
		self.x = initialPosition[0]
		self.y = initialPosition[1]
		self.deltaMovement = deltaMovement
		
	def getSprite(self):
		return self.sprite
		
	def getPosition(self):
		return (self.x, self.y)
		
	def moveUp(self):
		self.y -= self.deltaMovement
	def moveDown(self):
		self.y += self.deltaMovement

		
class Missile():
	def __init__(self, sprite):
		self.sprite = sprite
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
		
		planeSprite = pygame.image.load(os.path.join('sprites','plane.png'))
		self.plane = Plane(planeSprite, [200,150], 2)
		
		self.sprites["missile"] = pygame.image.load(os.path.join('sprites','missile.png'))

	def main_loop(self):
		while True:
			self.screen.fill((179, 253 ,255))
			self.clock.tick(60)
			
			keys = pygame.key.get_pressed()
			if keys[K_UP]:
				self.plane.moveUp()
			if keys[K_DOWN]:
				self.plane.moveDown()
			if keys[K_SPACE]:
				self.myMissiles.append([self.planePosition[0] + self.sprites["missile"].get_width(), self.planePosition[1]])
			
			for e in pygame.event.get():
				continue
			
			self.drawSprites()
			
			self.terrain.draw(self.screen)
			pygame.display.flip()
	
	def drawSprites(self):
		self.screen.blit(self.plane.getSprite(), self.plane.getPosition())
		for missile in self.myMissiles:
			self.screen.blit(self.sprites["missile"], missile)

	
if __name__ == '__main__':
	main = Main()
	main.main_loop()
