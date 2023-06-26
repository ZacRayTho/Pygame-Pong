import sys
import pygame as pg
from settings import *
from frog import *
from car import *
from float import *


bg = pg.image.load('bg.png')

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption('Frogger')
        self.frog = Frog(self)

        self.obstacles = [Car(self, 750, 550, -1, .04), Car(self, 950, 550, -1, .04), Car(self, 1150, 550, -1, .04),
                          Car(self, -500, 500, 1, .04), Car(self, -300, 500, 1, .04), Car(self, -100, 500, 1, .04),
                          Car(self, 850, 450, -1, .05), Car(self, 1050, 450, -1, .05), Car(self, 1250, 450, -1, .05),
                          Car(self, -350, 400, 1, .03), Car(self, -150, 400, 1, .03), Car(self, 50, 400, 1, .03),
                          Car(self, 800, 350, -1, .03), Car(self, 1000, 350, -1, .03), Car(self, 1200, 350, -1, .03),]
        
        self.ride = [Float(self, 750, 250, -1, .03, True)]

    def update(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT or event.key == ord('a'):
                    if self.frog.x != 0:
                        self.frog.x += -50
                        self.frog.y += 0
                if event.key == pg.K_RIGHT or event.key == ord('d'):
                    if self.frog.x != 650:
                        self.frog.x += 50
                        self.frog.y += 0
                if event.key == pg.K_UP or event.key == ord('w'):
                    if self.frog.y != 0:
                        self.frog.x += 0
                        self.frog.y += -50
                if event.key == pg.K_DOWN or event.key == ord('s'):
                    if self.frog.y != 600:
                        self.frog.x += 0
                        self.frog.y += 50

        pg.display.flip()
        self.frog.update()

        
        
        # self.car.update()
        # self.car2.update()
        # self.car3.update()

    def draw(self):
        self.screen.blit(bg, (0, 0))
        self.frog.draw()

        for x in self.obstacles:
            if x.hitbox.colliderect(self.frog.hitbox):
                print('Collision with', x)

            x.update()
            x.draw()

        for x in self.ride:
            if x.hitbox.colliderect(self.frog.hitbox):
                self.frog.x += x.speed * x.direction

            x.update()
            x.draw()

        # self.car.draw()
        # self.car2.draw()
        # self.car3.draw()


    def run(self):
        while True:
            self.update()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.run()
