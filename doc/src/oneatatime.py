from math import *

from scitools.easyviz import *

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

t = linspace(-10., 10., 41)

x,y = ndgrid(t,t)            
h = h0/(1+(x**2+y**2)/(R**2)) 

# The following four plots must run one at a time
mesh(x, y, h, savefig = 'images/simpleplotscitools.pdf')
#mesh(x, y, h, savefig = 'images/simpleplotscitools.png')
#surf(x, y, h, savefig = 'images/simpleplotcoloursscitools.pdf')
#surf(x, y, h, savefig = 'images/simpleplotcoloursscitools.png')