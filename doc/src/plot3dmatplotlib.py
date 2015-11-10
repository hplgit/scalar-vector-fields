import os
from math import *
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10*np.pi, 100)

fig = plt.figure() 
ax = fig.gca(projection = '3d')
ax.plot(np.sin(t), np.cos(t), t)
plt.title('Parametrized curve')
plt.savefig('images/parametrizedcurvematplotlib.pdf')
plt.savefig('images/parametrizedcurvematplotlib.png')
plt.show()

x = np.arange(-4, 4, 0.05, float)
y = np.arange(-2, 2, 0.05, float)
X, Y = np.meshgrid(x, y, sparse = False, indexing = 'ij')
Z = X*Y*np.sin(X*Y)

fig = plt.figure() 
ax = fig.gca(projection = '3d')
ax.plot_surface(X, Y, Z)
plt.title('Simple plot, no colours')
plt.savefig('images/simpleplotmatplotlib.pdf')
plt.savefig('images/simpleplotmatplotlib.png')
plt.show()

from matplotlib import cm

fig = plt.figure() 
ax = fig.gca(projection = '3d')
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
plt.title('Simple plot, with colours')
plt.savefig('images/simpleplotcoloursmatplotlib.pdf')
plt.savefig('images/simpleplotcoloursmatplotlib.png')
plt.show()

os.system('doconce combine_images pdf -2 images/simpleplotmatplotlib images/simpleplotcoloursmatplotlib images/plotmatplotlib')
os.system('doconce combine_images png -2 images/simpleplotmatplotlib images/simpleplotcoloursmatplotlib images/plotmatplotlib')

plt.contour(X, Y, Z)
plt.title('Simple contour plot')
plt.savefig('images/simplecontourmatplotlib.pdf')
plt.savefig('images/simplecontourmatplotlib.png')
plt.show()

plt.contour(X, Y, Z, 10)
plt.title('Contour plot, 10 levels')
plt.savefig('images/contour10levelsmatplotlib.pdf')
plt.savefig('images/contour10levelsmatplotlib.png')
plt.show()

plt.contour(X, Y, Z, 10, colors = 'k')
plt.title('Contour plot, 10 levels, in black')
plt.savefig('images/contour10levelsblackmatplotlib.pdf')
plt.savefig('images/contour10levelsblackmatplotlib.png')
plt.show()


levels = [0.1, 0.2, 0.3, 0.4]
plt.contour(X, Y, Z, levels = levels)
plt.title('Contour plot, with given levels')
plt.savefig('images/contourspeclevelsmatplotlib.pdf')
plt.savefig('images/contourspeclevelsmatplotlib.png')
plt.show()

cs = plt.contour(X, Y, Z)
plt.clabel(cs)
plt.title('Contour plot, with labels for the levels')
plt.savefig('images/contourclabelmatplotlib.pdf')
plt.savefig('images/contourclabelmatplotlib.png')
plt.show()

os.system('doconce combine_images pdf -2 images/contour10levelsmatplotlib images/contour10levelsblackmatplotlib images/contourspeclevelsmatplotlib images/contourclabelmatplotlib images/advancedcontourmatplotlib')
os.system('doconce combine_images png -2 images/contour10levelsmatplotlib images/contour10levelsblackmatplotlib images/contourspeclevelsmatplotlib images/contourclabelmatplotlib images/advancedcontourmatplotlib')

t = np.linspace(-5, 5, 11)
x, y = np.meshgrid(t, t, sparse = False, indexing = 'ij')
vx = x**2 + 2*y - .5*x*y
vy = -3*y
plt.quiver(x, y, vx, vy, angles = 'xy', scale_units = 'xy', color = 'b')
#plt.quiver(x, y, vx, vy, units='xy', scale=20, color='b') # skalareringsfaktor 1.5, blaa farge
plt.savefig('images/quivermatplotlibsimple.pdf')
plt.savefig('images/quivermatplotlibsimple.png')
plt.show()
#axis('equal')

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)
tt = np.linspace(-10., 10., 11)
xx, yy = np.meshgrid(tt, tt)       # Definer et grovere grid til vektorfeltet
hh = h0/(1+(xx**2 + yy**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(hh)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
plt.quiver(xx, yy, dhy, dhx, color = 'r', angles = 'xy')#, scale_units = 'xy') #, )

plt.hold('on')                     # Behold konturlinjene og akse-egenskapene
t = np.linspace(-10.,10.,21)

x, y = np.meshgrid(t, t)           # Grid for x- og y-verdiene (km)
h = h0/(1+(x**2+y**2)/(R**2))      # Beregn hoyden h (m)
plt.contour(x, y, h)               # Kontur og sett akseenhetene like
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('images/quivermatplotlibadvanced.pdf')
plt.savefig('images/quivermatplotlibadvanced.png')
plt.show()

os.system('doconce combine_images pdf -2 images/quivermatplotlibsimple images/quivermatplotlibadvanced images/quivermatplotlib')
os.system('doconce combine_images png -2 images/quivermatplotlibsimple images/quivermatplotlibadvanced images/quivermatplotlib')