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
	def __init__(self, sprite, initialPosition, deltaMovement):
		self.sprite = sprite
		self.x = initialPosition[0]
		self.y = initialPosition[1]
		self.deltaMovement = deltaMovement
		
	def getSprite(self):
		return self.sprite
		
	def getPosition(self):
		return (self.x, self.y)
	
	def applyForce(self):
		self.x += self.deltaMovement[0]
		self.y += self.deltaMovement[1]
	
		
		
class Main():

	sprites = {}
	myMissiles = []
	enemyMissiles = []
	clock	= None
	screen	= None
	deltaMovement = 2
	terrain = None
	def __init__(self):
		print "hello"
		pygame.init()

		pygame.display.set_caption('Wallstreet Tycoon')

		self.terrain = Terrain(100)
		self.screen = pygame.display.set_mode((800,400))
		self.clock = pygame.time.Clock()
		
		planeSprite = pygame.image.load(os.path.join('sprites','plane.png'))
		self.plane = Plane(planeSprite, [200,150], 2)
		self.sprites["myMissile"] = pygame.image.load(os.path.join('sprites','myMissile.png'))
		self.myMissileMovementSpeed = [5,0]

		

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
				self.myMissiles.append(Missile(self.sprites["myMissile"], self.plane.getPosition(), self.myMissileMovementSpeed))
			for e in pygame.event.get():
				continue
			self.drawSprites()
			
			self.applyForcesOfTheWorld()
			self.terrain.draw(self.screen)
			pygame.display.flip()
	
	
	def applyForcesOfTheWorld(self):
		for missile in self.myMissiles:
			missile.applyForce()
		
	def drawSprites(self):
		self.screen.blit(self.plane.getSprite(), self.plane.getPosition())
		for missile in self.myMissiles:
			self.screen.blit(missile.getSprite(), missile.getPosition())

	
if __name__ == '__main__':
	main = Main()
	main.main_loop()
