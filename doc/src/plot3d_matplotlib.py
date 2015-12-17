import os
from math import *
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

x = y = np.linspace(-5, 5, 11)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
xv_vec = xv**2 + 2*yv - .5*xv*yv
yv_vec = -3*yv
fig = plt.figure()
ax = fig.gca()
ax.quiver(xv, yv, xv_vec, yv_vec, angles='xy', color='b', scale_units='xy')
#plt.quiver(x, y, vx, vy, units='xy', scale=20, color='b') # skalareringsfaktor 1.5, blaa farge
plt.axis('equal')
plt.savefig('images/quivermatplotlibsimple.pdf')
plt.savefig('images/quivermatplotlibsimple.png')

x = y = np.linspace(-10.,10.,41)

xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)           # Grid for x- og y-verdiene (km)
hv = h0/(1 + (xv**2+yv**2)/(R**2))      # Beregn hoyden h (m)


x2 = y2 = np.linspace(-10., 10., 11)
x2v, y2v = np.meshgrid(x2, y2, indexing='ij', sparse=False)       # Definer et grovere grid til vektorfeltet
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # Beregn hoyden med det nye griddet
x2v_vec, y2v_vec = np.gradient(h2v)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
fig = plt.figure()
ax = fig.gca()
ax.quiver(x2v, y2v, x2v_vec, y2v_vec, color='r', angles='xy')#, scale_units = 'xy') #, )

plt.hold('on')                     # Behold konturlinjene og akse-egenskapene
x = y = np.linspace(-10.,10.,21)

xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)           # Grid for x- og y-verdiene (km)
hv = h0/(1+(xv**2+yv**2)/(R**2))      # Beregn hoyden h (m)
plt.contour(xv, yv, hv)               # Kontur og sett akseenhetene like
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('images/quivermatplotlibadvanced.pdf')
plt.savefig('images/quivermatplotlibadvanced.png')


fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv)
plt.savefig('images/defaultcontourmatplotlib.pdf')
plt.savefig('images/defaultcontourmatplotlib.png')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.contour(xv, yv, hv)
plt.savefig('images/defaultcontour3matplotlib.pdf')
plt.savefig('images/defaultcontour3matplotlib.png')

fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv, 10)
plt.savefig('images/contour10levelsmatplotlib.pdf')
plt.savefig('images/contour10levelsmatplotlib.png')

fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors='k')
plt.savefig('images/contour10levelsblackmatplotlib.pdf')
plt.savefig('images/contour10levelsblackmatplotlib.png')

fig = plt.figure()
ax = fig.gca()
levels = [500., 1000., 1500., 2000.]
ax.contour(xv, yv, hv, levels=levels)
plt.savefig('images/contourspeclevelsmatplotlib.pdf')
plt.savefig('images/contourspeclevelsmatplotlib.png')

fig = plt.figure()
ax = fig.gca()
cs = ax.contour(xv, yv, hv)
plt.clabel(cs)
plt.savefig('images/contourclabelmatplotlib.pdf')
plt.savefig('images/contourclabelmatplotlib.png')





fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv)
plt.savefig('images/simpleplotmatplotlib.pdf')
plt.savefig('images/simpleplotmatplotlib.png')



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm)

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

ax.plot(curve_x, curve_y, curve_z)


plt.savefig('images/simpleplotcoloursmatplotlib.pdf')
plt.savefig('images/simpleplotcoloursmatplotlib.png')



x = y = z = np.linspace(.5, 2., 8)
xv, yv, zv = np.meshgrid(x, y, z)
r3v = np.sqrt(xv**2 + yv**2 + zv**2)**3
xv_vec = -xv/r3v
yv_vec = -yv/r3v
zv_vec = -zv/r3v
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(xv, yv, zv, xv_vec, yv_vec, zv_vec, color='r', length=0.2)
plt.savefig('images/quivermatplotlibgr.png')
plt.savefig('images/quivermatplotlibgr.pdf')

plt.show()
