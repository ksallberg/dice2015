import pygame
from terrain import Terrain

class Main():

    clock    = None
    screen   = None
    terrain  = None #Terrain()

    def __init__(self):
        print "hello"
        pygame.init()
        pygame.display.set_caption('Wallstreet Tycoon')
        self.terrain = Terrain()
        self.screen = pygame.display.set_mode((500,
                                               300))
        self.clock = pygame.time.Clock()

    def main_loop(self):
        while True:
            print "hello im main loop"
            self.screen.fill((0,0,0))
            self.terrain.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.main_loop()
