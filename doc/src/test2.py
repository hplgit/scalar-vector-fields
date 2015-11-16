from scitools.easyviz import *
import os
#from math import *


#x, y, z = np.mgrid[.5:2:.2, .5:2:.2, .5:2:.2] nb_labels = 5, color = (0., 0., 0.))

t1 = linspace(0,2,3)
t2 = linspace(0,5,6)
x, y = meshgrid(t1, t2, sparse = False, indexing = 'ij')
print x, y

# scitools
x, y = ndgrid(t1, t2)
print x,  y