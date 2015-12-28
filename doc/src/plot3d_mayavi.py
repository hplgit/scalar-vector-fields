import mayavi.mlab as plt
import os
from math import *
import numpy as np

h0 = 2277.
R = 4.

xv, yv = np.mgrid[-10.:10.:.5, -10.:10.:.5]
hv = h0/(1 + (xv**2+yv**2)/(R**2))

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

# Simple plot of mountain
# Create a figure with white background and black foreground.
# Specify colors with RGB values: (0,0,0) for black,
# (1,1,1) for white.
# The foreground colour is used for text and labels included in the plot.
plt.figure(1, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.mesh(xv, yv, hv, extent=(0,1,0,1,0,1))
# Decorate the axes. nb_labels indetifies the number of marks on the axes.
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
# Decorate the plot with a title
plt.title('h(x,y)')

# Simple plot of mountain and parametric curve
plt.figure(2, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv, extent=(0,1,0,1,0,1))
# tube_radius controls the width of the parametrized curve.
# Increased here in order to make the curve more visible
# when shown together with `surf`.
plt.plot3d(curve_x, curve_y, curve_z, tube_radius=0.2, extent=(0,1,0,1,0,1))
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
# endsimpleplots

R2 = 10.
plt.figure(3, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.outline(plt.mesh(xv, yv, hv, extent=(0, 0.25, 0, 0.25, 0, 0.25), color=(.5, .5, .5)))
plt.outline(plt.mesh(xv, yv, hv, extent=(0.375, 0.625, 0, 0.25, 0, 0.25), colormap='Accent'))
plt.outline(plt.mesh(xv, yv, hv, extent=(0.75, 1, 0, 0.25, 0, 0.25), colormap='prism'))


h0 = 22.77
R = 4.

xv, yv = np.mgrid[-10.:10.:.5, -10.:10.:.5]
hv = h0/(1 + (xv**2+yv**2)/(R**2))

# Default contour plot plotted together with surface
plt.figure(4, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv)

# 10 contour lines (equally spaced contour levels)
plt.figure(5, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.contour_surf(xv, yv, hv, contours=10)

# 10 contour lines (equally spaced contour levels) together with surface
# Black color (i.e. (0., 0., 0.)) for contour lines.
plt.figure(6, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
s2 = plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv, contours=10, color=(0., 0., 0.))

# Specify the contour levels explicitly as a list
plt.figure(7, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
levels = [5., 10., 15., 20.]
plt.contour_surf(xv, yv, hv, contours=levels)
#end contourplots


x = y = z = np.linspace(.5, 2., 8)
xv, yv, zv = np.meshgrid(x, y, z, sparse=False, indexing='ij')
r3v = np.sqrt(xv**2 + yv**2 + zv**2)**3
u = -x/r3v
v = -y/r3v
w = -z/r3v
plt.figure(8, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.quiver3d(xv, yv, zv, u, v, w, mode='arrow', colormap='jet', scale_factor=.5)
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))

# Save figures to files
plt.figure(1)
plt.savefig('images/simple_plot_mayavi.png')

plt.figure(2)
plt.savefig('images/simple_plot_colours_mayavi.png')

plt.figure(3)
plt.savefig('images/subplot.png')

plt.figure(4)
plt.savefig('images/simple_contour_mayavi.png')

plt.figure(5)
plt.savefig('images/contour_10levels_mayavi.png')

plt.figure(6)
plt.savefig('images/contour_10levels_black_mayavi.png')

plt.figure(7)
plt.savefig('images/contour_speclevels_mayavi.png')

plt.figure(8)
plt.savefig('images/quiver_mayavi.png')