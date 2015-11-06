from mayavi.mlab import *
import os
from math import *
import numpy as np



clf()
figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
t = np.linspace(0, 10*np.pi, 100)
plot3d(np.sin(t), np.cos(t), t)
axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
title('My first plot')
savefig('images/parametrizedcurvemayavi.png')


x = np.arange(-4, 4, 0.05, float)
y = np.arange(-2, 2, 0.05, float)
X, Y = np.meshgrid(x, y, sparse = False, indexing = 'ij')
Z = X*Y*np.sin(X*Y)

clf()
mesh(X, Y, Z)
title('Using mesh')
axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
savefig('images/simpleplotmayavi.png')

clf()
surf(X, Y, Z)
title('Using surf')
axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
savefig('images/simpleplotcoloursmayavi.png')

#os.system('doconce combine_images png -2 images/simpleplotmayavi images/simpleplotcoloursmayavi images/plotmayavi')

clf()
surf1 = mesh(X-10, Y, Z, color = (.5, .5, .5))
cat1_extent = (-14, -6, -2, 2, -8, 8)
outline(surf1, extent=cat1_extent)

surf2 = mesh(X, Y, Z, colormap = 'Accent')
cat2_extent = (-4, 4, -2, 2, -8, 8)
outline(surf2, extent=cat2_extent)

surf3 = mesh(X+10, Y, Z, colormap = 'prism')
cat3_extent = (6, 14, -2, 2, -8, 8)
outline(surf3, extent=cat3_extent, color=(0.5, 0.5, 0.5))
savefig('images/subplot.png')


clf()
contour_surf(X, Y, Z)
savefig('images/simplecontourmayavi.png')

clf()
contour_surf(X, Y, Z, contours = 10)
savefig('images/contour10levelsmayavi.png')

clf()
contour_surf(X, Y, Z, contours = 10, color = (0., 0., 0.))
savefig('images/contour10levelsblackmayavi.png')

clf()
levels = [0.1, 0.2, 0.3, 0.4]
contour_surf(X, Y, Z, contours = levels)
savefig('images/contourspeclevelsmayavi.png')

#os.system('doconce combine_images png -2 images/simplecontourmayavi images/contour10levelsmayavi images/contour10levelsblackmayavi images/contourspeclevelsmayavi images/advancedcontourmayavi')

t = np.linspace(-5, 5, 11)
x, y = np.meshgrid(t, t, sparse = False, indexing = 'ij')
z = np.zeros_like(x)
vx = x**2 + 2*y - .5*x*y
vy = -3*y
vz = np.zeros_like(vx)
clf()
quiver3d(x, y, z, vx, vy, vz) #, angles = 'xy', scale_units = 'xy', color = 'b')
#quiver(x, y, vx, vy, units='xy', scale=20, color='b') # skalareringsfaktor 1.5, blaa farge
savefig('images/quivermayavi.png')
#quiver3d(x, y, z, u, v, w, line_width=3, scale_factor=1)

x, y, z = np.mgrid[-5:6, -5:6, -2:2:0.1]
vx = x**2 + 2*y - .5*x*y
vy = -3*y
vz = 0*z
clf()
flow(x, y, z, vx, vy, vz)
savefig('images/flowmayavi.png')