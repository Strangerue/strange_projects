# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 01:34:03 2021

@author: EVGEN
"""

import numpy as np
import matplotlib.pyplot as plt

def powe(z):
    a = (z.real * z. real) - (z.imag * z.imag)
    b = (z.imag * z.real) * 2
    x = np.complex(a, b)
    return x

def kard(fi):
    a = 1/4
    x = 2 * a * np.cos(fi) - a * np.cos(2 * fi)
    y = 2 * a * np.sin(fi) - a * np.sin(2 * fi)
    z = np.complex(x + 0.1, y)
    print(z)
    return z

z = np.complex(-1, 0)
c = np.complex(np.pi)
# c = kard(np.pi / )
x = []
y = []
for i in range(10000):
    x.append(z.real)
    y.append(z.imag)
    z = powe(z)
    x.append(z.real)
    y.append(z.imag)
    z += c
plt.figure()
#plt.axis([-1, 1, -1, 1])
plt.plot(x, y, '+', linewidth = 0.1)