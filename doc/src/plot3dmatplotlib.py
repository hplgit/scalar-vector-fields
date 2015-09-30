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




t = np.linspace(-5, 5, 11)
x, y = np.meshgrid(t, t, sparse = False, indexing = 'ij')
vx = x**2 + 2*y - .5*x*y
vy = -3*y
plt.quiver(x, y, vx, vy, angles = 'xy', scale_units = 'xy', color = 'b')
#plt.quiver(x, y, vx, vy, units='xy', scale=20, color='b') # skalareringsfaktor 1.5, blaa farge
plt.savefig('images/quivermatplotlib.pdf')
plt.savefig('images/quivermatplotlib.png')
plt.show()
#axis('equal')