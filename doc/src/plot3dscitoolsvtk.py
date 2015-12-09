from math import *
import numpy as np

from scitools.easyviz import quiver2, savefig

t2 = np.linspace(.5, 2., 8)
x, y, z = np.meshgrid(t2, t2, t2)
r3 = np.sqrt(x**2 + y**2 + z**2)**3
plt.quiver3(x, y, z, -x/r3, -y/r3, -z/r3, 0, 'r')
plt.savefig('images/quiverscitoolsgr.png')
plt.savefig('images/quiverscitoolsgr.pdf')

# system python plot3dscitoolsvtk.py --SCITOOLS_easyviz_backend vtk