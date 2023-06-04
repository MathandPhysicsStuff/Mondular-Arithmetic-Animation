import pygame
import sys 
from math import cos, sin ,pi

pygame.init()

clock = pygame.time.Clock()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))


run = True

while run:

    screen.fill((10, 10, 15))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
