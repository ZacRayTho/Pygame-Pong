import pygame as pg
from settings import *

class Frog:
    def __init__(self, game):
        self.game = game
        self.x, self.y = START_POS
        self.hitbox = pg.Rect(self.x, self.y, 50, 50)

    def draw(self):

        pg.draw.rect(self.game.screen, 'white', self.hitbox)

    def update(self):
        self.hitbox.update(self.x,self.y, 50,50)
        
        # keys = pg.key.get_pressed()
        # if keys[pg.K_w]:
        #     self.x += 0
        #     self.y += -50
        # if keys[pg.K_a]:
        #     pass
        # if keys[pg.K_s]:
        #     self.x += 0
        #     self.y += 50
        # if keys[pg.K_d]:            
        #     pass