import pygame
from pygame import gfxdraw,surfarray
import sys
import random
import time

pygame.init()
win = pygame.display.set_mode((500, 500))
B = (0, 0, 0)
W = (255, 255, 255)

cells = [[0 for i in range(50)] for i in range(50)]

def near(pos: list , system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count
    

while True:
    # time.sleep(0.05)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for i in range(-2, 3):
                for j in range(-2, 3):
                    cells[(pos[0]//10 + i) % 50][(pos[1]//10 + j) % 50] = random.randint(0, 1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            cells = [[random.randint(0, 1) for i in range(50)] for i in range(50)]
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            pos = pygame.mouse.get_pos()
            cells[pos[0]//10][pos[1]//10] = 1
            cells[pos[0]//10][pos[1]//10 + 1] = 1
            cells[pos[0]//10][pos[1]//10 - 1] = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            pos = pygame.mouse.get_pos()
            cells[pos[0]//10 -1][pos[1]//10 -1] = 1
            cells[pos[0]//10][pos[1]//10 +1] = 1
            cells[pos[0]//10][pos[1]//10] = 1
            cells[pos[0]//10 -1][pos[1]//10 +1] = 1
            cells[pos[0]//10 +1][pos[1]//10] = 1
    for i in range(0 , len(cells)):
        for j in range(0 , len(cells[i])):
            pygame.draw.rect(win , (255 * cells[i][j] % 256 , 255 * cells[i][j] % 256, 255 * cells[i][j] % 256) , [i * 10 , j * 10 , 10 , 10])
    # surfarray.blit_array(win, pic)
    pygame.display.update()
    cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if near([i , j]) not in (2 , 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if near([i , j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2