import pygame
from pygame import gfxdraw,surfarray
import sys

pygame.init()
win = pygame.display.set_mode((500, 500))

import numpy as np

def life(pic, i, j):
    a = 0
    if pic[i][j] == 0:
        if (pic[i-1][j-1]+pic[i][j-1]+pic[i+1][j-1]+pic[i-1][j]+
            pic[i+1][j]+pic[i-1][j+1]+pic[i][j+1]+pic[i+1][j+1] == 565):
            a = 255
    else:
        if (pic[i-1][j-1]+pic[i][j-1]+pic[i+1][j-1]+pic[i-1][j]+
            pic[i+1][j]+pic[i-1][j+1]+pic[i][j+1]+pic[i+1][j+1] < 310):
            a = 0
        if (pic[i-1][j-1]+pic[i][j-1]+pic[i+1][j-1]+pic[i-1][j]+
            pic[i+1][j]+pic[i-1][j+1]+pic[i][j+1]+pic[i+1][j+1] > 565):
            a = 0
    return a

img = np.zeros((500, 500))
i, j = 0, 0
# img = [[0 for i in range(250)] * 250]
while True:
    i += 1;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            img[pos[0], pos[1]] = 255
            img[pos[0], pos[1] + 1] = 255
            img[pos[0] + 1, pos[1]] = 255
            img[pos[0] + 1, pos[1] + 1] = 255
    img[i, j] = life(img, i, j)
    surfarray.blit_array(win, img)
    if i == 498:
        i = 0
        j += 1
    if j == 498: j = 0
    pygame.display.update()