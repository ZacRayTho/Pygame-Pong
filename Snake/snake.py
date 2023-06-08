import pygame as pg
from settings import *

class Snake:
    def __init__(self, game):
        self.game = game
        self.x, self.y = CENTER
    
    def movement(self):
        self.x += 0.25
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            


    def draw(self):
        pg.draw.circle(self.game.screen, 'white', (self.x , self.y), 50)
        
