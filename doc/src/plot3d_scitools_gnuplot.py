from math import *
import numpy as np

import scitools.easyviz as plt

h0 = 2277.  # Height of the top of the mountain (m)
R = 4.     # The radius of the mountain (km)

x = y = np.linspace(-10., 10., 41)

xv, yv = plt.ndgrid(x, y)
hv = h0/(1+(xv**2+yv**2)/(R**2))

plt.mesh(xv, yv, hv)
plt.savefig('images/simple_plot_scitools.png')
plt.savefig('images/simple_plot_scitools.pdf')

plt.contour3(xv, yv, hv, 10)
plt.savefig('images/default_contour3_scitools.png')
plt.savefig('images/default_contour3_scitools.pdf')

plt.surf(xv, yv, hv)
plt.hold('on')
s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))
plt.plot3(curve_x, curve_y, curve_z, 'r-')
plt.savefig('images/simple_plot_colours_scitools.png')
plt.savefig('images/simple_plot_colours_scitools.pdf')

