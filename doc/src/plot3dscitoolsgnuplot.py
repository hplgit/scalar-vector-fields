from math import *
import numpy as np

import scitools.easyviz as plt

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

t = np.linspace(-10., 10., 41)

x,y = plt.ndgrid(t,t)
h = h0/(1+(x**2+y**2)/(R**2))

# The following four plots must run one at a time
plt.mesh(x, y, h)
plt.savefig('images/simpleplotscitools.png')
plt.savefig('images/simpleplotscitools.pdf')

plt.surf(x, y, h)
plt.hold('on')
t = np.linspace(0, 2*np.pi, 100)
xcoords = 10*(1 - t/(2*np.pi))*np.cos(t)
ycoords = 10*(1 - t/(2*np.pi))*np.sin(t)
zcoords = h0/(1 + 100*(1 - t/(2*np.pi))**2/(R**2))
plt.plot3(xcoords, ycoords, zcoords, 'r-')
plt.savefig('images/simpleplotcoloursscitools.png')
plt.savefig('images/simpleplotcoloursscitools.pdf')