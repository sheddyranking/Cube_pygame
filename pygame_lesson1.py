import re
import pygame #the pygame.org/doc/ for the documentary 
import random
import sys


#initialling the pygame
pygame.init()

WIDTH = 800
HEIGTH = 600
RED = (250, 0, 0) #pygame takes only Rgb format
BLUE = (0, 0, 255)
player_size = 50
player_pos = [WIDTH/2, HEIGTH-2*player_size]
BACKGROUND_COLOR = (0,0,0)

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
SPEED = 10

#creating the display UI
screen = pygame.display.set_mode((WIDTH, HEIGTH))

#game loop

game_over = False

clock = pygame.time.Clock()

#drop enemies function
def drop_enemies(enemy_list):
    if len(enemy_list) < 10:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos,y_pos])

#draw enemies functions
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

#updating enemies position function
def updating_enemy_position(enemy_list):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] <= HEIGTH:
             enemy_pos[1] += SPEED 
        else:
            enemy_list.pop(idx)

#collision check
def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

#detect collision 
def detect_collision (player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[0]

    if(e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if(e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #traking the events left and right
        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y] #updating the new position

    screen.fill(BACKGROUND_COLOR) #its fills the sides black   

    #called the function
    if detect_collision(player_pos, enemy_pos):
        game_over = True
        break

    #drawing the rect shape.
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    #calling the functions
    drop_enemies(enemy_list)
    updating_enemy_position(enemy_list)

    if collision_check(enemy_list, player_pos):
        game_over =True
        break
    draw_enemies(enemy_list)

    pygame.display.update() #we need to unpdate the screen always 