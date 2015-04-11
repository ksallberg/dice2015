import pygame
import random

class Terrain():

    # a list of y coords
    point_amount = 100
    points = []
    x_space = 25
    mountain_height = 20

    # create some terrain points
    def __init__(self):
        for i in range(0, self.point_amount):
            self.points.append(1)

    # move all terrain steps to the left
    def move_terrain(self):
        self.points.insert(0, self.new_pos())
        self.points.pop()

    def new_pos(self):
        return (370 + random.randint(0, self.mountain_height) -
                      random.randint(0, self.mountain_height))

    # Draw the terrain to the context
    def draw(self, screen):
        self.move_terrain()
        for i in range(0, self.point_amount):
            red = (255,0,0)
            pygame.draw.rect(screen,
                             red,
                             (self.x_space * i, self.points[i],
                              self.x_space * i + 50, self.points[i] + 50),
                             1)
        print "draw terrain"
