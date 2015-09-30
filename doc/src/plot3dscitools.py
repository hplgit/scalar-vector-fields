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
savefig('contour10levelsblackscitools.png')
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

t = np.linspace(-5, 5, 11)
x,y = ndgrid(t, t)
vx = x**2 + 2*y - .5*x*y
vy = -3*y

quiver(x, y, vx, vy, 200, 'b')
axis('equal')
savefig('images/quiverscitools.pdf')
savefig('images/quiverscitools.png')
raw_input('press enter to continue')