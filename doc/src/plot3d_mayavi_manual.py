import mayavi.mlab as plt
import os
from math import *
import numpy as np

x = y = z = np.linspace(.5, 2., 6)
xv, yv, zv = np.meshgrid(x, y, z, sparse=False, indexing='ij')
rv = np.sqrt(xv**2 + yv**2 + zv**2)
u = -xv/rv**3
v = -yv/rv**3
w = -zv/rv**3

# Draw countours of 3D scalar field together with 3D vector field
plt.figure(11, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
# opacity controls how contours are visible through each other
plt.contour3d(xv, yv, zv, 1/rv**2, contours=10, opacity=0.5)
# scale_mode='none' says that the vectors should not be scaled
plt.quiver3d(xv, yv, zv, u, v, w, mode='arrow', colormap='jet',\
             scale_mode='none', opacity=0.5)
# end draw countours of 3D scalar field together with 3D vector field
raw_input('press enter to continue')