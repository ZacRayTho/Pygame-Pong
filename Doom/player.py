from settings import *
import pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        # Knowing the angle of the direction of the player, and the speed of his movement
        # We can calculate the increments dx, dy
        # by which the player's cordinates need to be changed
        # and for this we use trigonometric functions functions of sin,and cosine
        # dx = speed * cos(a) AND dy = speed * sin(a) for 'W' key movement 
        # dx = -speed * cos(a) AND dy = speed * sin(a) for 'A' key movement
        # dx = -speed * cos(a) AND dy = -speed * sin(a) for 'S' key movement
        # dx = speed * cos(a) AND dy = -speed * sin(a) for 'D' key movement
        # check out PlayerMovementDoom.png for pic
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        # to have player's movement speed independent of the framerate
        # need delta time, which is the amount of time that has passed sicne the last frame
        speed = PLAYER_SPEED * self.game.delta_time
        # precalculating the product of the obtained speed by the calculated values of the sin and cosine
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau # tau = 2 * pi

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        # the arguments passed to pygame.draw.line() specify
        #   - the screen to draw on
        #   - the color to draw the rectangle
        #   - the position of the line and multiplied by 100 for the size of each square on the mini_map, 
        #   - The ending point is calculated based on the starting point (self.x, self.y), the width of the line (WIDTH), and the angle at which the line is drawn (self.angle).
        #        The math.cos() and math.sin() functions are used to calculate the x and y components of the ending point based on the angle.
        #   - the width of the outline of the rectangle (set to 2 pixels)
        # # pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
        # #                 (self.x * 100 + WIDTH * math.cos(self.angle),
        # #                 self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        # the arguments passed to pygame.draw.rect() specify
        #   - the screen to draw on
        #   - the color to draw the circle
        #   - the position of the circle and multiplied by 100 for the size of each square on the mini_map, 
        #   - 15 specifies the radius of the circle
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y   

    @property
    def map_pos(self):
        return int(self.x), int(self.y)