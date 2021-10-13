# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 14:45:08 2021

@author: EVGEN
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc



rc('animation', html='html5')

fig = plt.figure(figsize=(10, 10))
plt.xticks([])
plt.yticks([])
max_frames = 200
max_zoom = 300
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

images = []
# кэш картинок

def init():
    return plt.gca()

def animate(i):
    if i > max_frames // 2:
        plt.imshow(images[max_frames//2-i], cmap='flag')
        print(3)
        return 
    
    if len(images) >= max_frames // 2:
        plt.imshow(images[i], cmap='flag')
        print(2)
        return 
    
    else:
        p_center, q_center = -0.793191078177363, 0.16093721735804
        zoom = (i / max_frames * 2)**3 * max_zoom + 1
        scalefactor = 1 / zoom
        pmin_ = (pmin - p_center) * scalefactor + p_center
        qmin_ = (qmin - q_center) * scalefactor + q_center
        pmax_ = (pmax - p_center) * scalefactor + p_center
        qmax_ = (qmax - q_center) * scalefactor + q_center
        image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)
        plt.imshow(image, cmap='flag')
        images.append(image)
    
    return plt.gca()

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints, 
               max_iterations=300, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k 
        z[mask] = np.nan
    return -image.T

# ani = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=max_frames, interval=1)
img = mandelbrot(pmin, pmax, 500, qmin, qmax, 500)
print(*img)
plt.imshow(img, cmap = 'flag')