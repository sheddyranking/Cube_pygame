import pygame
import sys

#initialling the pygame
pygame.init()

WIDTH = 800
HEIGTH = 600

#creating the display UI
screen = pygame.display.set_mode((WIDTH, HEIGTH))

#gamne loop

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #drawing the rect shape.
    pygame.draw.rect(screen, (250,0,0), (400, 300, 50, 50))

    pygame.display.update() #we need to unpdate the screen always 