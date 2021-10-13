import pygame
import multiprocessing
from pygame import gfxdraw,surfarray
import sys

pygame.init()
win = pygame.display.set_mode((500, 500))

import numpy as np
from numba import njit

I = (-1) ** .5
maxiter = 10

@njit(fastmath=True)
def f(z, c):
    return z * z + c

def cyc(val):
    for j in range(500):
        i0, j0 = val / scale + x, j / scale + y
        
        i0 = i0 / 250 * 2 - 2
        j0 = j0 / 250 * 2 - 2
        
        c = (i0 + j0 *I)
        
        z = 0
        
        for depth in range(maxiter):
            z = f(z, c)
            if abs(z) > 100:
                break

        c = depth * (255 / maxiter)% 255
        c1 = [(depth % 4 - 1) * 100, (depth % 2) * 100, (depth % 4 - 1) * 100]
        pic[val, j] = c1
    return pic

#@njit(fastmath=True)
def mandelbrot(x, y, scale):

    pic = np.zeros((500,500,3), dtype=np.float64)
    for i in range(500):
        pool_obj = multiprocessing.Pool()
        pic = pool_obj.map(cyc,range(500))
         #np.array([c.real, c.real, c.real], dtype=np.float64)

    return pic

x, y, scale = 0, 0, 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            scale *= 2
            pos = pygame.mouse.get_pos()
            print(pos)
            x1 = pos[0] / 500
            y1 = pos[1] / 500
            x = x + pos[0] / scale
            y = y + pos[1] / scale
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            pos = pygame.mouse.get_pos()
            print(pos)
            x1 = pos[0] / 500
            y1 = pos[1] / 500
            x = x - pos[0] / scale
            y = y - pos[1] / scale
            scale /= 2
            print(x, y, x1, y1)
    pic = mandelbrot(x, y, scale)
    surfarray.blit_array(win, pic)
    pygame.display.update()