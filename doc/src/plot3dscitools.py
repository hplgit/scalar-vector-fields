from math import *
import numpy as np

from scitools.easyviz import *
#from scitools.easyviz.gnuplot_ import *

#t = np.linspace(0, 10*np.pi, 100)
#plot3(np.sin(t), np.cos(t), t, title = 'Parametrized curve')
#raw_input('press enter to continue')

x = np.arange(-4, 4, 0.05, float)
y = np.arange(-2, 2, 0.05, float)
X, Y = ndgrid(x, y)
Z = X*Y*sin(X*Y)

# The following four plots must run one at a time
#mesh(X, Y, Z, title = 'Simple plot, no colours', savefig = 'images/simpleplotscitools.pdf')
#mesh(X, Y, Z, title = 'Simple plot, no colours', savefig = 'images/simpleplotscitools.png')
#surf(X, Y, Z, title = 'Simple plot, with colours', savefig = 'images/simpleplotcoloursscitools.pdf')
#surf(X, Y, Z, title = 'Simple plot, with colours', savefig = 'images/simpleplotcoloursscitools.png')

os.system('doconce combine_images pdf -2 images/simpleplotscitools images/simpleplotcoloursscitools images/plotscitools')
os.system('doconce combine_images png -2 images/simpleplotscitools images/simpleplotcoloursscitools images/plotscitools')

contour(X, Y, Z, title = 'Simple contour plot')
savefig('images/simplecontourscitools.pdf')
savefig('images/simplecontourscitools.png')
raw_input('press enter to continue')

contour(X, Y, Z, 10, title = 'Contour plot, 10 levels')
savefig('images/contour10levelsscitools.pdf')
savefig('images/contour10levelsscitools.png')
raw_input('press enter to continue')

contour(X, Y, Z, 10, 'k', title = 'Contour plot, 10 levels, in black')
savefig('images/contour10levelsblackscitools.pdf')
savefig('images/contour10levelsblackscitools.png')
raw_input('press enter to continue')

levels = [0.1, 0.2, 0.3, 0.4]
contour(X, Y, Z, levels = levels, title = 'Contour plot, with given levels')
savefig('images/contourspeclevelsscitools.pdf')
savefig('images/contourspeclevelsscitools.png')
raw_input('press enter to continue')

contour(X, Y, Z, clabels = 'on', title = 'Contour plot, with labels for the levels')
savefig('images/contourclabelscitools.pdf')
savefig('images/contourclabelscitools.png')
raw_input('press enter to continue')

os.system('doconce combine_images pdf -2 images/contour10levelsscitools images/contour10levelsblackscitools images/contourspeclevelsscitools images/contourclabelscitools images/advancedcontourscitools')
os.system('doconce combine_images png -2 images/contour10levelsscitools images/contour10levelsblackscitools images/contourspeclevelsscitools images/contourclabelscitools images/advancedcontourscitools')

t = np.linspace(-5, 5, 11)
x,y = ndgrid(t, t)
vx = x**2 + 2*y - .5*x*y
vy = -3*y

quiver(x, y, vx, vy, 200, 'b')
axis('equal')
savefig('images/quiverscitoolssimple.pdf')
savefig('images/quiverscitoolssimple.png')
raw_input('press enter to continue')


h0 = 2277  # Hoyden av toppen av fjellet (m)
R = 4      # Maal for radius av fjellet (km)
tt = linspace(-10.,10.,11)
xx,yy = ndgrid(tt, tt)      # Definer et grovere grid til vektorfeltet
hh = h0/(1+(xx**2+yy**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(hh)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
quiver(xx, yy, dhx, dhy, 0, 'r')
hold('on')                    # Behold konturlinjene og akse-egenskapene
t = linspace(-10., 10., 21)

x,y = ndgrid(t,t)             # Grid for x- og y-verdiene (km)
h = h0/(1+(x**2+y**2)/(R**2)) # Beregn hoyden h (m)
contour(x, y, h, daspectmode = 'equal')  # Kontur og sett akseenhetene like
xlabel('x')
ylabel('y')
axis('equal')
hold('off')
# Sett aksenavn
# Sett akseenhetene like
# Trenger ikke flere plott i denne figuren
savefig('images/quiverscitoolsadvanced.pdf')
savefig('images/quiverscitoolsadvanced.png')
raw_input('Press enter to continue')

os.system('doconce combine_images pdf -2 images/quiverscitoolssimple images/quiverscitoolsadvanced images/quiverscitools')
os.system('doconce combine_images png -2 images/quiverscitoolssimple images/quiverscitoolsadvanced images/quiverscitools')