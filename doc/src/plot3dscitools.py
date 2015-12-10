from math import *
import numpy as np

import scitools.easyviz as plt
#from scitools.easyviz.gnuplot_ import *

#t = np.linspace(0, 10*np.pi, 100)
#plot3(np.sin(t), np.cos(t), t, title = 'Parametrized curve')

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

x = y = np.linspace(-10., 10., 41)

xv, yv = plt.ndgrid(x, y)             # Grid for x- og y-verdiene (km)
hv = h0/(1+(xv**2+yv**2)/(R**2)) # Beregn hoyden h (m)

plt.contour(xv, yv, hv)
plt.savefig('images/defaultcontourscitools.pdf')
plt.savefig('images/defaultcontourscitools.png')

plt.contour(xv, yv, hv, 10)
plt.savefig('images/contour10levelsscitools.pdf')
plt.savefig('images/contour10levelsscitools.png')

plt.contour(xv, yv, hv, 10, 'k')
plt.savefig('images/contour10levelsblackscitools.pdf')
plt.savefig('images/contour10levelsblackscitools.png')

levels = [500., 1000., 1500., 2000.]
plt.contour(xv, yv, hv, levels=levels)
plt.savefig('images/contourspeclevelsscitools.pdf')
plt.savefig('images/contourspeclevelsscitools.png')

plt.contour(xv, yv, hv, clabels='on')
plt.savefig('images/contourclabelscitools.pdf')
plt.savefig('images/contourclabelscitools.png')

x = y = np.linspace(-5, 5, 11)
xv, yv = plt.ndgrid(x, y)
xv_vec = xv**2 + 2*yv - .5*xv*yv
yv_vec = -3*yv

plt.quiver(xv, yv, xv_vec, yv_vec, 200, 'b')
plt.axis('equal')
plt.savefig('images/quiverscitoolssimple.pdf')
plt.savefig('images/quiverscitoolssimple.png')


x = y = np.linspace(-10.,10.,11)
x2v, y2v = plt.ndgrid(x, y)      # Definer et grovere grid til vektorfeltet
h2v = h0/(1+(x2v**2+y2v**2)/(R**2)) # Beregn hoyden med det nye griddet
x2v_vec, y2v_vec = np.gradient(h2v)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
plt.quiver(x2v, y2v, x2v_vec, y2v_vec, 0, 'r')
plt.hold('on')                    # Behold konturlinjene og akse-egenskapene
x = y = np.linspace(-10., 10., 21)

xv, yv = plt.ndgrid(x, y)             # Grid for x- og y-verdiene (km)
hv = h0/(1+(xv**2+yv**2)/(R**2)) # Beregn hoyden h (m)
plt.contour(xv, yv, hv)  # Kontur og sett akseenhetene like
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.hold('off')
# Sett aksenavn
# Sett akseenhetene like
# Trenger ikke flere plott i denne figuren
plt.savefig('images/quiverscitoolsadvanced.pdf')
plt.savefig('images/quiverscitoolsadvanced.png')