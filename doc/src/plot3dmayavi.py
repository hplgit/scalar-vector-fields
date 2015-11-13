import mayavi.mlab as ml
import os
from math import *
import numpy as np

h0 = 2277.
R = 4.

x, y = np.mgrid[-10.:10.:.5, -10.:10.:.5] 
h = h0/(1 + (x**2+y**2)/(R**2))

ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
ml.mesh(x, y, h, extent = (0,1,0,1,0,1))
ml.axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
ml.savefig('images/simpleplotmayavi.png')


ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
ml.surf(x, y, h, extent = (0,1,0,1,0,1))

t = np.linspace(0, 2*np.pi, 100)
xcoords = 10*(1 - t/(2*np.pi))*np.cos(t)
ycoords = 10*(1 - t/(2*np.pi))*np.sin(t)
zcoords = h0/(1 + 100*(1 - t/(2*np.pi))**2/(R**2))
ml.plot3d(xcoords, ycoords, zcoords, tube_radius = 0.2, extent = (0,1,0,1,0,1))

ml.axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
ml.savefig('images/simpleplotcoloursmayavi.png')
#os.system('doconce combine_images png -2 images/simpleplotmayavi images/simpleplotcoloursmayavi images/plotmayavi')

R2 = 10.
ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
surf1 = ml.mesh(x, y, h, extent = (0, 0.25, 0, 0.25, 0, 0.25), color = (.5, .5, .5))
cat1_extent = (0, 0.25, 0, 0.25, 0, 0.25)
ml.outline(surf1, extent = cat1_extent)

surf2 = ml.mesh(x, y, h, extent = (0.375, 0.625, 0, 0.25, 0, 0.25), colormap = 'Accent')
cat2_extent = (0.375, 0.625, 0, 0.25, 0, 0.25)
ml.outline(surf2, extent = cat2_extent)

surf3 = ml.mesh(x, y, h, extent = (0.75, 1, 0, 0.25, 0, 0.25), colormap = 'prism')
cat3_extent = (0.75, 1, 0, 0.25, 0, 0.25)
ml.outline(surf3, extent = cat3_extent, color = (0.5, 0.5, 0.5))
ml.savefig('images/subplot.png')


ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
ml.surf(x, y, h, extent = (0,1,0,1,0,1))
ml.contour_surf(x, y, h, extent = (0,1,0,1,0,1))
ml.savefig('images/simplecontourmayavi.png')

ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
ml.contour_surf(x, y, h, extent = (0,1,0,1,0,1), contours = 10)
ml.savefig('images/contour10levelsmayavi.png')

ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
ml.surf(x, y, h, extent = (0,1,0,1,0,1))
ml.contour_surf(x, y, h, extent = (0,1,0,1,0,1), contours = 10, color = (0., 0., 0.))
ml.savefig('images/contour10levelsblackmayavi.png')

ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0))
levels = [500., 1000., 1500., 2000.]
ml.contour_surf(x, y, h, extent = (0,1,0,1,0,1), contours = levels)
ml.savefig('images/contourspeclevelsmayavi.png')

#os.system('doconce combine_images png -2 images/simplecontourmayavi images/contour10levelsmayavi images/contour10levelsblackmayavi images/contourspeclevelsmayavi images/advancedcontourmayavi')

x, y, z = np.mgrid[.5:2:.2, .5:2:.2, .5:2:.2]
r3 = np.sqrt(x**2 + y**2 + z**2)**3
ml.figure(fgcolor = (.0, .0, .0), bgcolor = (1.0, 1.0, 1.0)) 
ml.quiver3d(x, y, z, -x/r3, -y/r3, -z/r3, mode = 'arrow', colormap = 'jet', scale_factor = .5)
ml.axes(xlabel = 'x', ylabel = 'y', zlabel = 'z', nb_labels = 5, color = (0., 0., 0.))
ml.savefig('images/quivermayavi.png')