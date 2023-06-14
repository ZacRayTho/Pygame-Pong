import pygame as pg

class Car:
    def __init__(self, game, xstart, ystart, direction, speed):
        self.game = game
        self.x = xstart
        self.y = ystart
        self.direction = direction
        self.speed = speed
        self.hitbox = pg.Rect(self.x, self.y, 50, 50)

    def draw(self):
        pg.draw.rect(self.game.screen, 'white', self.hitbox)

            
    def update(self):
        self.hitbox.update(self.x,self.y, 50,50)
        if self.direction == -1:
            if self.x < -100:
                self.x = 700
            else:
                self.x += self.speed * self.direction
        else:
            if self.x > 750:
                self.x = -50
            else:
                self.x += self.speed * self.direction