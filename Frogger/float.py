import pygame as pg

class Float:
    def __init__(self, game, xstart, ystart, direction, speed, solid):
        self.game = game
        self.x = xstart
        self.y = ystart
        self.direction = direction
        self.speed = speed
        # randomize log length?
        self.hitbox = pg.Rect(self.x, self.y, 50, 50)
        # solid attr will decide between log or frog that goes in and out
        self.solid = solid

    def draw(self):
        pg.draw.rect(self.game.screen, 'brown', self.hitbox)

            
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
