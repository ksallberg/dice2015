import pygame
import random

class Terrain():

    # a list of y coords
    point_amount = 20
    points = []
    x_space = 50

    # create some terrain points
    def __init__(self, mountain_height):
        self.mountain_height = mountain_height
        for i in range(0, self.point_amount):
            self.points.append(self.new_pos())

    # move all terrain steps to the left
    def move_terrain(self):
        self.points.append(self.new_pos())
        self.points.pop(0)

    def new_pos(self):
        return (300 + random.randint(0, self.mountain_height) -
                      random.randint(0, self.mountain_height))

    # Draw the terrain to the context
    def draw(self, screen):
        self.move_terrain()
        vertices = [(0,screen.get_height())]
        for i in range(0, self.point_amount):
            red = (204, 161, 131)
            # Populate vertices
            vertices.append((i * self.x_space, self.points[i]))
        vertices.append((screen.get_width(), screen.get_height()))
        vertices.append((0,screen.get_height()))
        pygame.draw.polygon(screen,
                            red,
                            vertices,
                            0)
