import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface, pause, player):
        for x in range(self.rows):
            for y in range(self.columns):
                if(player == -1):
                    y_pos = y * self.scale
                    x_pos = x * self.scale
                    #random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                    if self.grid_array[x][y] == 1:
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                elif(player == 2):
                    y_pos = y * self.scale
                    x_pos = x * self.scale
                    if(x < 10):
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    elif self.grid_array[x][y] == 1:
                        pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

                else:
                    oijxc = 5/0


        def check_winner(self):
            player_1_count = 0
            player_2_count = 0
            
            for x in range(self.rows):
                for y in range(self.columns):
                    if self.grid_array[x][y] == 1 and x < 10:
                        player_1_count += 1
        
            for x in range(self.rows):
                for y in range(self.columns):
                    if self.grid_array[x][y] == 1 and x > self.columns - 10:
                        player_2_count += 1

            if player_1_count > player_2_count:
                return 1
            elif player_2_count > player_1_count:
                return 2
            else:
                return 0


        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next

    def HandleMouse(self, x, y):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = 1
        

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
