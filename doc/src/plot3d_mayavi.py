import mayavi.mlab as plt
import os
from math import *
import numpy as np

h0 = 2277.
R = 4.

xv, yv = np.mgrid[-10.:10.:.5, -10.:10.:.5]
hv = h0/(1 + (xv**2+yv**2)/(R**2))

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.mesh(xv, yv, hv, extent=(0,1,0,1,0,1))
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/simple_plot_mayavi.png')


xv, yv = np.mgrid[-10.:10.:.5, -10.:10.:.5]
hv = h0/(1 + (xv**2+yv**2)/(R**2))
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv, extent=(0,1,0,1,0,1))

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))
plt.plot3d(curve_x, curve_y, curve_z, tube_radius=0.2, extent=(0,1,0,1,0,1))

plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/simple_plot_colours_mayavi.png')

R2 = 10.
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.outline(plt.mesh(xv, yv, hv, extent=(0, 0.25, 0, 0.25, 0, 0.25), color=(.5, .5, .5)))
plt.outline(plt.mesh(xv, yv, hv, extent=(0.375, 0.625, 0, 0.25, 0, 0.25), colormap='Accent'))
plt.outline(plt.mesh(xv, yv, hv, extent=(0.75, 1, 0, 0.25, 0, 0.25), colormap='prism'))

plt.savefig('images/subplot.png')

h0 = 22.77
R = 4.

xv, yv = np.mgrid[-10.:10.:.5, -10.:10.:.5]
hv = h0/(1 + (xv**2+yv**2)/(R**2))

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv)
plt.savefig('images/simple_contour_mayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.contour_surf(xv, yv, hv, contours=10)
plt.savefig('images/contour_10levels_mayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
s2 = plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv, contours=10, color=(0., 0., 0.))
plt.savefig('images/contour_10levels_black_mayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
levels = [5., 10., 15., 20.]
plt.contour_surf(xv, yv, hv, contours=levels)
plt.savefig('images/contour_speclevels_mayavi.png')

x = y = z = np.linspace(.5, 2., 8)
xv, yv, zv = np.meshgrid(x, y, z)
r3v = np.sqrt(xv**2 + yv**2 + zv**2)**3
xv_vec = -x/r3v
yv_vec = -y/r3v
zv_vec = -z/r3v
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0)) 
plt.quiver3d(xv, yv, zv, xv_vec, yv_vec, zv_vec, mode='arrow', colormap='jet', scale_factor=.5)
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/quiver_mayavi.png')