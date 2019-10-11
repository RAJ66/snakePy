import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))

snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = (random.randint(0,590),random.randint(0,590))

snake = [(200, 200), (210, 200), (220, 200)]
my_directio = LEFT

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()
