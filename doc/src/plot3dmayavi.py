import mayavi.mlab as plt
import os
from math import *
import numpy as np

h0 = 2277.
R = 4.

x, y = np.mgrid[-10.:10.:.5, -10.:10.:.5] 
h = h0/(1 + (x**2+y**2)/(R**2))

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.mesh(x, y, h, extent=(0,1,0,1,0,1))
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/simpleplotmayavi.png')


x, y = np.mgrid[-10.:10.:.5, -10.:10.:.5] 
h = h0/(1 + (x**2+y**2)/(R**2))
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(x, y, h, extent=(0,1,0,1,0,1))

t = np.linspace(0, 2*np.pi, 100)
xcoords = 10*(1 - t/(2*np.pi))*np.cos(t)
ycoords = 10*(1 - t/(2*np.pi))*np.sin(t)
zcoords = h0/(1 + 100*(1 - t/(2*np.pi))**2/(R**2))
plt.plot3d(xcoords, ycoords, zcoords, tube_radius=0.2, extent=(0,1,0,1,0,1))

plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/simpleplotcoloursmayavi.png')

R2 = 10.
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.outline(plt.mesh(x, y, h, extent=(0, 0.25, 0, 0.25, 0, 0.25), color=(.5, .5, .5)))
plt.outline(plt.mesh(x, y, h, extent=(0.375, 0.625, 0, 0.25, 0, 0.25), colormap='Accent'))
plt.outline(plt.mesh(x, y, h, extent=(0.75, 1, 0, 0.25, 0, 0.25), colormap='prism'))

plt.savefig('images/subplot.png')

h0 = 22.77
R = 4.

x, y = np.mgrid[-10.:10.:.5, -10.:10.:.5] 
h = h0/(1 + (x**2+y**2)/(R**2))

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(x, y, h)
plt.contour_surf(x, y, h)
plt.savefig('images/simplecontourmayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.contour_surf(x, y, h, contours=10)
plt.savefig('images/contour10levelsmayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
s2 = plt.surf(x, y, h)
plt.contour_surf(x, y, h, contours=10, color=(0., 0., 0.))
plt.savefig('images/contour10levelsblackmayavi.png')

plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
levels = [5., 10., 15., 20.]
plt.contour_surf(x, y, h, contours=levels)

x, y, z = np.mgrid[.5:2:.2, .5:2:.2, .5:2:.2]
r3 = np.sqrt(x**2 + y**2 + z**2)**3
plt.figure(fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0)) 
plt.quiver3d(x, y, z, -x/r3, -y/r3, -z/r3, mode='arrow', colormap='jet', scale_factor=.5)
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5, color=(0., 0., 0.))
plt.savefig('images/quivermayavi.png')