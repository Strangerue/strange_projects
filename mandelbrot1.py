# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 03:38:50 2021

@author: EVGEN
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure()
A = 0

for i in np.arange(0, 2 * np.pi, np.pi / 180):
    fi = i
    q = []
    w = []
    a = 1/4
    x = 2 * a * np.cos(fi) - a * np.cos(2 * fi)
    y = 2 * a * np.sin(fi) - a * np.sin(2 * fi)
    x_1 = np.cos(np.radians(A)) * 0.5
    y_1 = np.sin(np.radians(A)) * 0.5
    q.append(x)
    q.append(x_1)
    w.append(y)
    w.append(y_1)
    if i == 0:
        print(q, w)
    A += 1
    z = np.complex(x, y)
    plt.plot(q, w, linewidth = 0.5, color = 'r')