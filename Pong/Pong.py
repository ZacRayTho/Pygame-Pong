import pygame
from sys import exit

# Initializes all the stuff pygame needs to run
pygame.init()

# sets the screen size(width, height)
# all 'screens' are surfaces 
screen = pygame.display.set_mode((500, 500))

# sets name of pygame screen and icon
pygame.display.set_caption('Pong')
icon = pygame.image.load('./zt-light-logo.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

background = pygame.Surface((15,100))
ball_back = pygame.Surface((15,15))

left_pong = pygame.Surface((15,100))
left_pong.fill('white')
left_pos = left_pong.get_rect()
left_pos = left_pos.move(5, 200)
screen.blit(left_pong, left_pos)

right_pong = pygame.Surface((15,100))
right_pong.fill('white')
right_pos = right_pong.get_rect()
right_pos = right_pos.move(480, 200)
screen.blit(right_pong, right_pos)

ball = pygame.Surface((15, 15))
ball.fill('white')

ball_pos = ball.get_rect()
ball_pos = ball_pos.move(243.5, 243.5)
direction = True
height = True
# print(ball_pos)
# (243.5, 243.5)
left_wins = 0
right_wins = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # we need sys exit because pygame.quit doesnt close the for loop
            exit()

    # blit stands for block image transfer, put one surface on another
    # takes surface, and position

    
    if ball_pos.colliderect(right_pos) or ball_pos.colliderect(left_pos):
        direction = not direction

    if direction == True:
        if ball_pos.right > 500:
            left_wins = left_wins + 1
            print("Left Score: ", left_wins)
            direction = False
            screen.blit(ball_back, ball_pos)
            ball_pos.update(243, 243, 15, 15)
            screen.blit(ball, ball_pos)
        screen.blit(ball_back, ball_pos)
        ball_pos = ball_pos.move(3, 0)
        screen.blit(ball, ball_pos)
    elif direction == False:
        if ball_pos.left < 0: 
            right_wins = right_wins + 1
            print("Right Score: ", right_wins)
            direction = True
            screen.blit(ball_back, ball_pos)
            ball_pos.update(243, 243, 15, 15)
            screen.blit(ball, ball_pos)
        screen.blit(ball_back, ball_pos)
        ball_pos = ball_pos.move(-3, 0)
        screen.blit(ball, ball_pos)

    if height == True:
        if ball_pos.bottom > 500:
            height = False
        screen.blit(ball_back, ball_pos)
        ball_pos = ball_pos.move(0, 3)
        screen.blit(ball, ball_pos)
    elif height == False:
        if ball_pos.top < 0: 
            height = True
        screen.blit(ball_back, ball_pos)
        ball_pos = ball_pos.move(0, -3)
        screen.blit(ball, ball_pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        screen.blit(background, left_pos)
        if left_pos.top > 0:
            left_pos = left_pos.move(0, -5)
        screen.blit(left_pong, left_pos)

    if keys[pygame.K_UP]:
        screen.blit(background, right_pos)
        if right_pos.top > 0:
            right_pos = right_pos.move(0, -5)
        screen.blit(right_pong, right_pos)

    if keys[pygame.K_s]:
        screen.blit(background, left_pos)
        if left_pos.bottom < 500:
            left_pos = left_pos.move(0, 5)
        screen.blit(left_pong, left_pos)

    if keys[pygame.K_DOWN]:
        screen.blit(background, right_pos)
        if right_pos.bottom < 500:
            right_pos = right_pos.move(0, 5)
        screen.blit(right_pong, right_pos)

    
    pygame.display.update()

    # tick caps top framerate to prevent game from running too fast
    clock.tick(60)
