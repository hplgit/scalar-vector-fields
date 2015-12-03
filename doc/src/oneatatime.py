from math import *

from scitools.easyviz import *

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

t = linspace(-10., 10., 41)

x,y = ndgrid(t,t)            
h = h0/(1+(x**2+y**2)/(R**2)) 

# The following four plots must run one at a time
mesh(x, y, h, savefig = 'images/simpleplotscitools.png')

surf(x, y, h)
hold('on')
plot3([1,2], [1,2], [1, 2])
t = linspace(0, 2*pi, 100)
xcoords = 10*(1 - t/(2*pi))*cos(t)
ycoords = 10*(1 - t/(2*pi))*sin(t)
zcoords = h0/(1 + 100*(1 - t/(2*pi))**2/(R**2))
raw_input('press enter')
plot3(xcoords, ycoords, zcoords, 'r-')
raw_input('press enter')
savefig('images/simpleplotcoloursscitools.png')