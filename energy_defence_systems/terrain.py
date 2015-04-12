import pygame
import random

class Terrain():

    # create some terrain points
    def __init__(self, mountain_height, color, baseline):
        self.point_amount = 35
        self.points = []
        self.vertices = []
        self.x_space = 25
        self.mountain_height = mountain_height
        self.color = color
        self.baseline = baseline
        for i in range(0, self.point_amount):
            self.points.append(self.new_pos())

    # move all terrain steps to the left
    def move_terrain(self):
        self.points.append(self.new_pos())
        self.points.pop(0)

    def new_pos(self):
        return (self.baseline + random.randint(0, self.mountain_height) -
                                random.randint(0, self.mountain_height))

    # Draw the terrain to the context
    def draw(self, screen):
        self.vertices = [[0,screen.get_height()]]
        for i in range(0, self.point_amount):
            # Populate vertices
            self.vertices.append([i * self.x_space, self.points[i]])
        self.vertices.append([screen.get_width(), screen.get_height()])
        self.vertices.append([0,screen.get_height()])
        pygame.draw.polygon(screen,
                            self.color,
                            self.vertices,
                            0)
