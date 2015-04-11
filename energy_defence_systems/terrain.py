import pygame
import random

class Terrain():

    # a list of y coords
    point_amount = 10
    points = []
    x_space = 25

    # create some terrain points
    def __init__(self):
        for i in range(0, self.point_amount):
            self.points.append(1)

    # move all terrain steps to the left
    def move_terrain(self):
        self.points.insert(0, self.new_pos())
        self.points.pop()

    def new_pos(self):
        return self.points[0] + random.randint(0, 5) - random.randint(0, 5)

    # Draw the terrain to the context
    def draw(self, screen):
        self.move_terrain()
        for x in range(0, self.point_amount):
            red = (255,0,0)
            pygame.draw.rect(screen, red, (20, 20,50,50), 20)
        print "draw terrain"
