import pygame
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *

class Game:
    def __init__(self):
        # this function called whenever a new Game class is made, it initializes pygame modules
        # then it makes a window with res settings in settings, and make a clock object
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        # create instance of map class, passing self into it
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)

    def update(self):
        # flip function updates entire screen
        # tick function sets fps cap based on settings FPS variable
        # set caption function sets the caption of the window equal to the fps the game is running at
        # ':.1f' indicates that the value should be formatted as a floating-point number with one decimal place.
        self.player.update()
        self.raycasting.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        # this function checks for if the game window is closed and shuts down the pygame modules and kills the while loop in the run method
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        # this is the main loop of the game that calls the other methods
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    # this makes a Game class and starts the game with run method
    game = Game()
    game.run()
