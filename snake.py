import pygame
import random
from pygame.locals import *


def on_grid_rando():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return(x//10*10, y//10*10)


def collision(c1, c2):
    return (c1[0] == c2[0])and(c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))

snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_pos = (on_grid_rando())

snake = [(200, 200), (210, 200), (220, 200)]
my_directio = LEFT
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_directio = UP
            if event.key == K_DOWN:
                my_directio = DOWN
            if event.key == K_LEFT:
                my_directio = LEFT
            if event.key == K_RIGHT:
                my_directio = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_rando()
        snake.append((0, 0))
        score = score+1

    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()
        exit()

    for i in range(1, len(snake)-1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()
            exit()

    for i in range(len(snake)-1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_directio == UP:
        snake[0] = (snake[0][0], snake[0][1]-10)
    if my_directio == DOWN:
        snake[0] = (snake[0][0], snake[0][1]+10)
    if my_directio == RIGHT:
        snake[0] = (snake[0][0]+10, snake[0][1])
    if my_directio == LEFT:
        snake[0] = (snake[0][0]-10, snake[0][1])

    screen.fill((0, 0, 0))

    screen.blit(apple, apple_pos)

    for x in range(0, 600, 10):  # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
    for y in range(0, 600, 10):  # Draw vertical lines
        pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)

    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
