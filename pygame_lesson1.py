import pygame #the pygame.org/doc/ for the documentary 
import sys

#initialling the pygame
pygame.init()

WIDTH = 800
HEIGTH = 600
RED = (250, 0, 0) #pygame takes only Rgb format
player_pos = [400, 300]
player_size = 50

#creating the display UI
screen = pygame.display.set_mode((WIDTH, HEIGTH))

#game loop

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #traking the events left and right
        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.type == pygame.K_LEFT:
                x -= 5
            elif event.type == pygame.K_RIGHT:
                x += 5
            player_pos = [x, y] #updating the new position

    #drawing the rect shape.
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update() #we need to unpdate the screen always 