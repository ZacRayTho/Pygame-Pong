import pygame as pg
from settings import *

class Snake:
    def __init__(self, game):
        self.game = game
        self.x, self.y = CENTER
        self.x_change = 0
        self.y_change = 0
        self.old_pos = (0, 0)
    
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.x_change = 0.00
            self.y_change = -0.25
        if keys[pg.K_a]:
            self.x_change = -0.25
            self.y_change = 0.00
        if keys[pg.K_s]:
            self.x_change = 0.00
            self.y_change = 0.25
        if keys[pg.K_d]:
            self.x_change = 0.25
            self.y_change = 0.00
        self.x += self.x_change 
        self.y += self.y_change
            


    def draw(self):
        pg.draw.circle(self.game.screen, 'white', (self.x , self.y), 50)
        
