from math import *
import numpy as np

import scitools.easyviz as plt

h0 = 2277.  # Height of the top of the mountain (m)
R = 4.     # The radius of the mountain (km)

x = y = np.linspace(-10., 10., 41)
xv, yv = plt.ndgrid(x, y)
hv = h0/(1+(xv**2+yv**2)/(R**2))

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

# Simple plot of mountain
plt.figure(1)
plt.mesh(xv, yv, hv)

# Simple plot of mountain and parametric curve
plt.figure(2)
plt.surf(xv, yv, hv)
plt.hold('on')

# add the parametric curve. Last parameter controls color of the curve
plt.plot3(curve_x, curve_y, curve_z, 'b-')
# endsimpleplots

# Default two-dimensional contour plot
plt.figure(3)
plt.contour(xv, yv, hv)

# Default three-dimensional contour plot
plt.figure(4)
plt.contour3(xv, yv, hv, 10)

# 10 contour lines (equally spaced contour levels)
plt.figure(5)
plt.contour(xv, yv, hv, 10)

# 10 black ('k') contour lines
plt.figure(6)
plt.contour(xv, yv, hv, 10, 'k')

# Specify the contour levels explicitly as a list
plt.figure(7)
levels = [500., 1000., 1500., 2000.]
plt.contour(xv, yv, hv, levels=levels)

# Add labels with the contour level for each contour line
plt.figure(8)
plt.contour(xv, yv, hv, clabels='on')
#end contourplots

plt.figure(1)
plt.savefig('images/simple_plot_scitools.png')
plt.savefig('images/simple_plot_scitools.pdf')

plt.figure(2)
plt.savefig('images/simple_plot_colours_scitools.png')
plt.savefig('images/simple_plot_colours_scitools.pdf')

plt.figure(3)
plt.savefig('images/default_contour_scitools.pdf')
plt.savefig('images/default_contour_scitools.png')

plt.figure(4)
plt.savefig('images/default_contour3_scitools.png')
plt.savefig('images/default_contour3_scitools.pdf')

plt.figure(5)
plt.savefig('images/contour_10levels_scitools.pdf')
plt.savefig('images/contour_10levels_scitools.png')

plt.figure(6)
plt.savefig('images/contour_10levels_black_scitools.pdf')
plt.savefig('images/contour_10levels_black_scitools.png')

plt.figure(7)
plt.savefig('images/contour_speclevels_scitools.pdf')
plt.savefig('images/contour_speclevels_scitools.png')

plt.figure(8)
plt.savefig('images/contour_clabel_scitools.pdf')
plt.savefig('images/contour_clabel_scitools.png')
