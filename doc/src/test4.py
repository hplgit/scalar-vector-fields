import numpy as np

import matplotlib.pyplot as plt

print np.version.version
h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)


tt = np.linspace(-10., 10., 11)
#xx, yy = np.meshgrid(tt, tt)       # Definer et grovere grid til vektorfeltet
xx, yy = np.meshgrid(tt, tt, indexing = 'ij')
hh = h0/(1 + (xx**2 + yy**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(hh)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
plt.quiver(xx, yy, dhx, dhy, color = 'r', angles = 'xy')#, color = 'r', angles = 'xy')#, scale_units = 'xy') #, )
plt.show()