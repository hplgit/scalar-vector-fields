import os
from math import *
import numpy as np

import matplotlib.pyplot as plt

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

t = np.linspace(-5, 5, 11)
x, y = np.meshgrid(t, t, sparse=False, indexing='ij')
vx = x**2 + 2*y - .5*x*y
vy = -3*y
ax = plt.gca()
ax.quiver(x, y, vx, vy, angles='xy', color='b', scale_units='xy')
#plt.quiver(x, y, vx, vy, units='xy', scale=20, color='b') # skalareringsfaktor 1.5, blaa farge
plt.axis('equal')
plt.savefig('images/quivermatplotlibsimple.pdf')
plt.savefig('images/quivermatplotlibsimple.png')

t = np.linspace(-10.,10.,41)

x, y = np.meshgrid(t, t, indexing='ij', sparse=False)           # Grid for x- og y-verdiene (km)
h = h0/(1 + (x**2+y**2)/(R**2))      # Beregn hoyden h (m)


t2 = np.linspace(-10., 10., 11)
x2, y2 = np.meshgrid(t2, t2, indexing='ij', sparse=False)       # Definer et grovere grid til vektorfeltet
h2 = h0/(1 + (x2**2 + y2**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(h2)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
ax = plt.gca()
ax.quiver(x2, y2, dhx, dhy, color='r', angles='xy')#, scale_units = 'xy') #, )

plt.hold('on')                     # Behold konturlinjene og akse-egenskapene
t = np.linspace(-10.,10.,21)

x, y = np.meshgrid(t, t, indexing='ij', sparse=False)           # Grid for x- og y-verdiene (km)
h = h0/(1+(x**2+y**2)/(R**2))      # Beregn hoyden h (m)
plt.contour(x, y, h)               # Kontur og sett akseenhetene like
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('images/quivermatplotlibadvanced.pdf')
plt.savefig('images/quivermatplotlibadvanced.png')

from mpl_toolkits.mplot3d import Axes3D





fig = plt.figure() 
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, h)
plt.savefig('images/simpleplotmatplotlib.pdf')
plt.savefig('images/simpleplotmatplotlib.png')

from matplotlib import cm

fig = plt.figure() 
ax = fig.gca(projection='3d')
ax.plot_surface(x, y, h, cmap=cm.coolwarm)

t = np.linspace(0, 2*np.pi, 100)
xcoords = 10*(1 - t/(2*np.pi))*np.cos(t)
ycoords = 10*(1 - t/(2*np.pi))*np.sin(t)
zcoords = h0/(1 + 100*(1 - t/(2*np.pi))**2/(R**2))

ax.plot(xcoords, ycoords, zcoords)


plt.savefig('images/simpleplotcoloursmatplotlib.pdf')
plt.savefig('images/simpleplotcoloursmatplotlib.png')

plt.contour(x, y, h)
plt.savefig('images/simplecontourmatplotlib.pdf')
plt.savefig('images/simplecontourmatplotlib.png')

plt.contour(x, y, h, 10)
plt.savefig('images/contour10levelsmatplotlib.pdf')
plt.savefig('images/contour10levelsmatplotlib.png')

plt.contour(x, y, h, 10, colors='k')
plt.savefig('images/contour10levelsblackmatplotlib.pdf')
plt.savefig('images/contour10levelsblackmatplotlib.png')


levels = [500., 1000., 1500., 2000.]
plt.contour(x, y, h, levels=levels)
plt.savefig('images/contourspeclevelsmatplotlib.pdf')
plt.savefig('images/contourspeclevelsmatplotlib.png')

cs = plt.contour(x, y, h)
plt.clabel(cs)
plt.savefig('images/contourclabelmatplotlib.pdf')
plt.savefig('images/contourclabelmatplotlib.png')
