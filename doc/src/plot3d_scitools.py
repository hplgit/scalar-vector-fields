from math import *
import numpy as np

import scitools.easyviz as plt
#from scitools.easyviz.gnuplot_ import *


h0 = 2277.  # Height of the top of the mountain (m)
R = 4.     # The radius of the mountain (km)

x = y = np.linspace(-10., 10., 41)

xv, yv = plt.ndgrid(x, y)             # Grid for x, y values (km)
hv = h0/(1+(xv**2+yv**2)/(R**2)) # Compute height (m)

plt.contour(xv, yv, hv)
plt.savefig('images/default_contour_scitools.pdf')
plt.savefig('images/default_contour_scitools.png')

plt.contour(xv, yv, hv, 10)
plt.savefig('images/contour_10levels_scitools.pdf')
plt.savefig('images/contour_10levels_scitools.png')

plt.contour(xv, yv, hv, 10, 'k')
plt.savefig('images/contour_10levels_black_scitools.pdf')
plt.savefig('images/contour_10levels_black_scitools.png')

levels = [500., 1000., 1500., 2000.]
plt.contour(xv, yv, hv, levels=levels)
plt.savefig('images/contour_speclevels_scitools.pdf')
plt.savefig('images/contour_speclevels_scitools.png')

plt.contour(xv, yv, hv, clabels='on')
plt.savefig('images/contour_clabel_scitools.pdf')
plt.savefig('images/contour_clabel_scitools.png')

x = y = np.linspace(-5, 5, 11)
xv, yv = plt.ndgrid(x, y)
u = xv**2 + 2*yv - .5*xv*yv
v = -3*yv

plt.quiver(xv, yv, u, v, 200, 'b')
plt.axis('equal')
plt.savefig('images/quiver_scitools_simple.pdf')
plt.savefig('images/quiver_scitools_simple.png')


x = y = np.linspace(-10.,10.,11)
x2v, y2v = plt.ndgrid(x, y)      # Define a coarser grid for the vector field
h2v = h0/(1+(x2v**2+y2v**2)/(R**2)) # Compute height for new grid
dhdx, dhdy = np.gradient(h2v)         # Compute the gradient vector (dh/dx,dh/dy)
# Plot the vector field (red color) and scale the lengths of the vectors with a factor
# A better scaling factor is .75, but may not work?
plt.quiver(x2v, y2v, dhdx, dhdy, 0, 'r')
plt.hold('on')
x = y = np.linspace(-10., 10., 21)

xv, yv = plt.ndgrid(x, y)             # Grid for x, y values (km)
hv = h0/(1+(xv**2+yv**2)/(R**2)) # Compute height (m)
plt.contour(xv, yv, hv)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.hold('off')
plt.savefig('images/quiver_scitools_advanced.pdf')
plt.savefig('images/quiver_scitools_advanced.png')