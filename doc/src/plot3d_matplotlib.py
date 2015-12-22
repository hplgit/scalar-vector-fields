import os
from math import *
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

h0 = 2277.   # Height of the top of the mountain (m)
R = 4.      # The radius of the mountain (km)

x = y = np.linspace(-5, 5, 11)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
xv_vec = xv**2 + 2*yv - .5*xv*yv
yv_vec = -3*yv
fig = plt.figure()
ax = fig.gca()
ax.quiver(xv, yv, xv_vec, yv_vec, angles='xy', color='b', scale_units='xy')
#plt.quiver(x, y, vx, vy, units='xy', scale=20, color='b') # scale factor 1.5, blue color
plt.axis('equal')
plt.savefig('images/quiver_matplotlib_simple.pdf')
plt.savefig('images/quiver_matplotlib_simple.png')

x = y = np.linspace(-10.,10.,41)

xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)           # Grid for x, y values (km)
hv = h0/(1 + (xv**2+yv**2)/(R**2))      # Compute height (m)


x2 = y2 = np.linspace(-10., 10., 11)
x2v, y2v = np.meshgrid(x2, y2, indexing='ij', sparse=False)       # Define a coarser grid for the vector field
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # Compute height for new grid
x2v_vec, y2v_vec = np.gradient(h2v)         # Compute the gradient vector (dh/dx,dh/dy)
# Plot the vector field (red color) and scale the lengths of the vectors with a factor
# A better scaling factor is .75, but may not work?
fig = plt.figure()
ax = fig.gca()
ax.quiver(x2v, y2v, x2v_vec, y2v_vec, color='r', angles='xy')#, scale_units = 'xy') #, )

plt.hold('on')
x = y = np.linspace(-10.,10.,21)

xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)           # Grid for x, y values (km)
hv = h0/(1+(xv**2+yv**2)/(R**2))      # Compute height (m)
plt.contour(xv, yv, hv)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.savefig('images/quiver_matplotlib_advanced.pdf')
plt.savefig('images/quiver_matplotlib_advanced.png')


fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv)
plt.savefig('images/default_contour_matplotlib.pdf')
plt.savefig('images/default_contour_matplotlib.png')

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.contour(xv, yv, hv)
plt.savefig('images/default_contour3_matplotlib.pdf')
plt.savefig('images/default_contour3_matplotlib.png')

fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv, 10)
plt.savefig('images/contour_10levels_matplotlib.pdf')
plt.savefig('images/contour_10levels_matplotlib.png')

fig = plt.figure()
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors='k')
plt.savefig('images/contour_10levels_black_matplotlib.pdf')
plt.savefig('images/contour_10levels_black_matplotlib.png')

fig = plt.figure()
ax = fig.gca()
levels = [500., 1000., 1500., 2000.]
ax.contour(xv, yv, hv, levels=levels)
plt.savefig('images/contour_speclevels_matplotlib.pdf')
plt.savefig('images/contour_speclevels_matplotlib.png')

fig = plt.figure()
ax = fig.gca()
cs = ax.contour(xv, yv, hv)
plt.clabel(cs)
plt.savefig('images/contour_clabel_matplotlib.pdf')
plt.savefig('images/contour_clabel_matplotlib.png')





fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv)
plt.savefig('images/simple_plot_matplotlib.pdf')
plt.savefig('images/simple_plot_matplotlib.png')



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm)

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

ax.plot(curve_x, curve_y, curve_z)


plt.savefig('images/simple_plot_colours_matplotlib.pdf')
plt.savefig('images/simple_plot_colours_matplotlib.png')



x = y = z = np.linspace(.5, 2., 8)
xv, yv, zv = np.meshgrid(x, y, z)
r3v = np.sqrt(xv**2 + yv**2 + zv**2)**3
xv_vec = -xv/r3v
yv_vec = -yv/r3v
zv_vec = -zv/r3v
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.quiver(xv, yv, zv, xv_vec, yv_vec, zv_vec, color='r', length=0.2)
plt.savefig('images/quiver_matplotlib_gr.png')
plt.savefig('images/quiver_matplotlib_gr.pdf')

plt.show()
