from math import *
import numpy as np

import scitools.easyviz as plt
#from scitools.easyviz.gnuplot_ import *

#t = np.linspace(0, 10*np.pi, 100)
#plot3(np.sin(t), np.cos(t), t, title = 'Parametrized curve')
#raw_input('press enter to continue')

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

t = np.linspace(-10., 10., 41)

x,y = plt.ndgrid(t,t)             # Grid for x- og y-verdiene (km)
h = h0/(1+(x**2+y**2)/(R**2)) # Beregn hoyden h (m)



plt.contour(x, y, h)
plt.savefig('images/simplecontourscitools.pdf')
plt.savefig('images/simplecontourscitools.png')
raw_input('press enter to continue')

plt.contour(x, y, h, 10)
plt.savefig('images/contour10levelsscitools.pdf')
plt.savefig('images/contour10levelsscitools.png')
raw_input('press enter to continue')

plt.contour(x, y, h, 10, 'k')
plt.savefig('images/contour10levelsblackscitools.pdf')
plt.savefig('images/contour10levelsblackscitools.png')
raw_input('press enter to continue')

levels = [500., 1000., 1500., 2000.]
plt.contour(x, y, h, levels=levels)
plt.savefig('images/contourspeclevelsscitools.pdf')
plt.savefig('images/contourspeclevelsscitools.png')
raw_input('press enter to continue')

plt.contour(x, y, h, clabels='on')
plt.savefig('images/contourclabelscitools.pdf')
plt.savefig('images/contourclabelscitools.png')
raw_input('press enter to continue')

t = np.linspace(-5, 5, 11)
x,y = plt.ndgrid(t, t)
vx = x**2 + 2*y - .5*x*y
vy = -3*y

plt.quiver(x, y, vx, vy, 200, 'b')
plt.axis('equal')
plt.savefig('images/quiverscitoolssimple.pdf')
plt.savefig('images/quiverscitoolssimple.png')
raw_input('press enter to continue')


tt = np.linspace(-10.,10.,11)
xx,yy = plt.ndgrid(tt, tt)      # Definer et grovere grid til vektorfeltet
hh = h0/(1+(xx**2+yy**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(hh)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
plt.quiver(xx, yy, dhx, dhy, 0, 'r')
plt.hold('on')                    # Behold konturlinjene og akse-egenskapene
t = np.linspace(-10., 10., 21)

x,y = plt.ndgrid(t,t)             # Grid for x- og y-verdiene (km)
h = h0/(1+(x**2+y**2)/(R**2)) # Beregn hoyden h (m)
plt.contour(x, y, h)  # Kontur og sett akseenhetene like
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.hold('off')
# Sett aksenavn
# Sett akseenhetene like
# Trenger ikke flere plott i denne figuren
plt.savefig('images/quiverscitoolsadvanced.pdf')
plt.savefig('images/quiverscitoolsadvanced.png')
raw_input('Press enter to continue')
