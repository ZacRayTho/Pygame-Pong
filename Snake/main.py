import pygame as pg
import sys
from settings import *
from snake import *
from map import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.snake = Snake(self)
        self.map = Map(self)

    def draw(self):
        self.screen.fill('black')
        self.snake.draw()
        self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        pg.display.flip()
        self.snake.movement()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
