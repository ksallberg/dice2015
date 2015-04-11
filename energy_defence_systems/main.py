import pygame
import os.path
import random
from pygame.locals import *
from terrain import Terrain
from random import randint


class Cannon():
	def __init__(self, sprite, initialPosition, deltaMovement, timeToWaitUntilShoot):
		self.sprite = sprite
		self.x = initialPosition[0]
		self.y = initialPosition[1]
		self.deltaMovement = deltaMovement
		self.waittime = timeToWaitUntilShoot
		self.timeAtInstantiating = pygame.time.get_ticks()
		self.fired = False
		
	def getSprite(self):
		return self.sprite
	def getPosition(self):
		return (self.x, self.y)
	def shoot(self):
		if ((self.timeAtInstantiating + self.waittime) - pygame.time.get_ticks() < 0) and not self.fired:
			self.fired = True
			return True
		else:
			return False
	def applyForce(self):
		self.x += self.deltaMovement[0]
		self.y += self.deltaMovement[1]
		
	
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
	cannons = []
	clock	= None
	screen	= None
	deltaMovement = 2
	terrain = None
	DRAWTERRAIN = USEREVENT + 1

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
		self.sprites["enemyMissile"] = pygame.image.load(os.path.join('sprites','enemyMissile.png'))
		self.sprites["cannon"] = pygame.image.load(os.path.join('sprites','cannon.png'))
		self.myMissileMovementSpeed = [5,0]
		self.enemyMissileMovementSpeed = [0, -2]
		self.gameOver = False
		pygame.time.set_timer(self.DRAWTERRAIN, 50)

		

	def main_loop(self):
		while not self.gameOver:
			self.screen.fill((179, 253 ,255))
			self.clock.tick(60)
			
			keys = pygame.key.get_pressed()
			if keys[K_UP]:
				self.plane.moveUp()
			if keys[K_DOWN]:
				self.plane.moveDown()
			for e in pygame.event.get():
				if e.type == self.DRAWTERRAIN:
					self.terrain.move_terrain()
					print "Move terrain"
				if e.type == KEYDOWN:
					if e.key == K_SPACE:
						self.myMissiles.append(Missile(self.sprites["myMissile"], self.plane.getPosition(), self.myMissileMovementSpeed))

			self.terrain.draw(self.screen)
			self.drawOrRemoveSprites()
			self.applyForcesOfTheWorld()
			self.checkIfCannonsShouldShoot()
			pygame.display.flip()
			if random.randint(0,100) == 1:
				self.cannons.append(Cannon(self.sprites['cannon'], [850,320], (-3,0), random.randint(1000,4000)))
	
		
		
	def checkIfCannonsShouldShoot(self):
		for cannon in self.cannons:
			if cannon.shoot():
				self.enemyMissiles.append(Missile(self.sprites["enemyMissile"], cannon.getPosition(), self.enemyMissileMovementSpeed))
	
	def checkCollisionWithShip(self):
		for missile in enemyMissiles:
			if pygame.sprite.collide_mask(self.plane.getSprite(), self.missile.getSprite()):
				self.gameOver = True
				break

	def applyForcesOfTheWorld(self):
		for missile in self.myMissiles:
			missile.applyForce()

		for missile in self.enemyMissiles:
			missile.applyForce()

			
		for cannon in self.cannons:
			cannon.applyForce()

	def removeObjectsFromList(self, listOfItemsToRemove, originalList):
		for item in listOfItemsToRemove:
			originalList.remove(item)
			
	def drawOrRemoveSprites(self):
		removeObjects = []
		for missile in self.myMissiles:
			if missile.getPosition()[0] > self.screen.get_width:
				removeObjects.append(self.myMissles)
			else:
				self.screen.blit(missile.getSprite(), missile.getPosition())
		
		self.removeObjectsFromList(removeObjects, self.myMissiles)
		
		removeObjects = []
		
		for cannon in self.cannons:
			if cannon.getPosition()[0] < 0:
				removeObjects.append(cannon)
			else:
				self.screen.blit(cannon.getSprite(), cannon.getPosition())
		
		self.removeObjectsFromList(removeObjects, self.cannons)

		
		removeObjects = []
			
		for missile in self.enemyMissiles:
			if missile.getPosition()[1] < 0:
				removeObjects.append(missile)
			else:
				self.screen.blit(missile.getSprite(), missile.getPosition())
		
		self.removeObjectsFromList(removeObjects, self.enemyMissiles)

		self.screen.blit(self.plane.getSprite(), self.plane.getPosition())

	
if __name__ == '__main__':
	main = Main()
	main.main_loop()
