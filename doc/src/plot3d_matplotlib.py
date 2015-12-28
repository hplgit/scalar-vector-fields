import os
from math import *
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

h0 = 2277.   # Height of the top of the mountain (m)
R = 4.       # Radius of the mountain (km)
#endinitvalues

# Grid two-dimensional vector field
x = y = np.linspace(-5, 5, 11)
xv, yv = np.meshgrid(x, y, sparse=False, indexing='ij')
u = xv**2 + 2*yv - .5*xv*yv
v = -3*yv
# endtwodimfield

# Draw 2D-field
fig = plt.figure(1)
ax = fig.gca()
# The parameters angles and scale_units ensure here that the vectors
# are drawn with the same units as the x,y-coordinates
ax.quiver(xv, yv, u, v, angles='xy', color='b', scale_units='xy')
plt.axis('equal')
# end draw 2D-field

# Grid for x, y values (km)
x = y = np.linspace(-10.,10.,41)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)
# indexing='ij' means an $xy$-coordinate system.
# indexing='xy' means coordinates as row/column indices in a matrix.
hv = h0/(1 + (xv**2+yv**2)/(R**2))      # Elevation coordinates (m)
# endinitgrid

# Define a coarser grid for the vector field
x2 = y2 = np.linspace(-10.,10.,21)
x2v, y2v = np.meshgrid(x2, y2, indexing='ij', sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # Surface on coarse grid
# endcoarsergrid

dhdx, dhdy = np.gradient(h2v) # dh/dx, dh/dy
# endgradient

# Plot the vector field (red color) and scale the lengths of the vectors with a factor
# A better scaling factor is .75, but may not work?

x = y = np.linspace(-10.,10.,21)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)           # Grid for x, y values (km)
hv = h0/(1+(xv**2+yv**2)/(R**2))      # Compute height (m)

# Draw contours and gradient field of h
fig = plt.figure(2)
ax = fig.gca()
ax.quiver(x2v, y2v, dhdx, dhdy, color='r', angles='xy', scale_units='xy')
plt.contour(xv, yv, hv)
plt.axis('equal')
# end draw contours and gradient field of h


# Default two-dimensional contour plot with 7 colored lines
fig = plt.figure(3)
ax = fig.gca()
ax.contour(xv, yv, hv)

# Default three-dimensional contour plot
fig = plt.figure(4)
ax = fig.gca(projection='3d')
ax.contour(xv, yv, hv)

# 10 contour lines (equally spaced contour levels)
fig = plt.figure(5)
ax = fig.gca()
ax.contour(xv, yv, hv, 10)

# 10 black ('k') contour lines
fig = plt.figure(6)
ax = fig.gca()
ax.contour(xv, yv, hv, 10, colors='k')

# Specify the contour levels explicitly as a list
fig = plt.figure(7)
ax = fig.gca()
levels = [500., 1000., 1500., 2000.]
ax.contour(xv, yv, hv, levels=levels)

# Add labels with the contour level for each contour line
fig = plt.figure(8)
ax = fig.gca()
cs = ax.contour(xv, yv, hv)
plt.clabel(cs)
#end contourplots





s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))
# endparamcurve

# Simple plot of mountain
from matplotlib import cm

fig = plt.figure(9)
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.coolwarm, rstride=2, cstride=2)

# Simple plot of mountain and parametric curve
fig = plt.figure(10)
ax = fig.gca(projection='3d')
ax.plot_surface(xv, yv, hv, cmap=cm.Spectral, rstride=1, cstride=1)
# add the parametric curve. linewidth controls the width of the curve
ax.plot(curve_x, curve_y, curve_z, linewidth=5)
# endsimpleplots


# Grid three-dimensional vector field
x = y = z = np.linspace(.5, 2., 8)
xv, yv, zv = np.meshgrid(x, y, z, sparse=False, indexing='ij')
r3v = np.sqrt(xv**2 + yv**2 + zv**2)**3
u = -xv/r3v
v = -yv/r3v
w = -zv/r3v
# endthreedimfield

# Draw 3D-field
fig = plt.figure(11)
ax = fig.gca(projection='3d')
ax.quiver(xv, yv, zv, u, v, w, color='r', length=0.2)
# end draw 3D-field

plt.figure(1)
plt.savefig('images/quiver_matplotlib_simple.pdf')
plt.savefig('images/quiver_matplotlib_simple.png')

plt.figure(2)
plt.savefig('images/quiver_matplotlib_advanced.pdf')
plt.savefig('images/quiver_matplotlib_advanced.png')

plt.figure(3)
plt.savefig('images/default_contour_matplotlib.pdf')
plt.savefig('images/default_contour_matplotlib.png')

plt.figure(4)
plt.savefig('images/default_contour3_matplotlib.pdf')
plt.savefig('images/default_contour3_matplotlib.png')

plt.figure(5)
plt.savefig('images/contour_10levels_matplotlib.pdf')
plt.savefig('images/contour_10levels_matplotlib.png')

plt.figure(6)
plt.savefig('images/contour_10levels_black_matplotlib.pdf')
plt.savefig('images/contour_10levels_black_matplotlib.png')

plt.figure(7)
plt.savefig('images/contour_speclevels_matplotlib.pdf')
plt.savefig('images/contour_speclevels_matplotlib.png')

plt.figure(8)
plt.savefig('images/contour_clabel_matplotlib.pdf')
plt.savefig('images/contour_clabel_matplotlib.png')

plt.figure(9)
plt.savefig('images/simple_plot_matplotlib.pdf')
plt.savefig('images/simple_plot_matplotlib.png')


plt.figure(10)
plt.savefig('images/simple_plot_colours_matplotlib.pdf')
plt.savefig('images/simple_plot_colours_matplotlib.png')

plt.figure(11)
plt.savefig('images/quiver_matplotlib_gr.png')
plt.savefig('images/quiver_matplotlib_gr.pdf')
