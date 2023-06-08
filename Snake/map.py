import pygame as pg

class Map:
    def __init__(self, game):
        self.game = game
        self.size = 1000

    def draw(self):
        for x in range(self.size):
            if x%100 == 0:
                for y in range(self.size):
                    if y%100 == 0: 
                        pg.draw.rect(self.game.screen, 'darkgray', (x , y, 100, 100), 2)

