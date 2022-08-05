import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

total_frames = 0

#resolution
width, height = 1000,800
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 50

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 30
offset = 1

GameGrid = grid.Grid(width,height, scaler, offset)
# Grid.random2d_array()

pause = True

for player_id in range(1, 3):
    run = True
    pygame.display.set_caption(f"CONWAY'S GAME OF LIFE -- PLAYER {player_id}")    

    while run:
        clock.tick(fps)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause

        if(player_id == 1):
            GameGrid.Conway(off_color=white, on_color=blue1, surface=screen, pause=True, player=-1)
        if(player_id == 2):
            GameGrid.Conway(off_color=white, on_color=blue1, surface=screen, pause=True, player=2)

        if(player_id == 1):
            if pygame.mouse.get_pressed()[0]:
                mouseX, mouseY = pygame.mouse.get_pos()
                if(mouseX / scaler < 10):
                    GameGrid.HandleMouse(mouseX, mouseY)
        elif (player_id ==2):
            if pygame.mouse.get_pressed()[0]:

                mouseX, mouseY = pygame.mouse.get_pos()
                if(mouseX / scaler > (width / scaler) - 10):
                    GameGrid.HandleMouse(mouseX, mouseY)

        else:
            oidsf = 5/0


        pygame.display.update()

        
        if player_id == 1 and not run:
            pygame.display.set_caption(f"SWITCH PLAYERS")   
            #make the display black 
            pygame.draw.rect(screen, black, [0, 0, width, height])
            pygame.display.update()
            screen_hide = True
            while screen_hide:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        screen_hide = False
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            screen_hide = False
                    



pygame.display.set_caption(f"CONWAY'S GAME OF LIFE")    
run = True
pause = False


while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    GameGrid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause, player=-1)



    pygame.display.update()

    if not pause:
        total_frames+= 1
    if total_frames % 100 == 0:
        print(total_frames)
    if total_frames > 500:
        run = False
# result = str(GameGrid.check_winner())
result = "Jeff"
pygame.display.set_caption(f"CONWAY'S GAME OF LIFE -- GAME OVER -- PLAYER " + result + " WON")    

close_window = False
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                close_window = True
    pygame.display.update()
pygame.quit()
