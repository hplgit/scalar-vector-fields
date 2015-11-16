from scitools.easyviz import *

h0 = 2277.  # Hoyden av toppen av fjellet (m)
R = 4.      # Maal for radius av fjellet (km)

tt = linspace(-10.,10.,11)
xx,yy = ndgrid(tt, tt)      # Definer et grovere grid til vektorfeltet
hh = h0/(1+(xx**2+yy**2)/(R**2)) # Beregn hoyden med det nye griddet
dhx, dhy = np.gradient(hh)         # Beregn gradientvektoren (dh/dx,dh/dy)
# Plott vektorfeltet (rod farge) og skaler vektorlengden med en faktor
# En bedre skaleringsfaktor er .75, men fungerer kanskje ikke?
quiver(xx, yy, dhx, dhy, 0, 'r')

raw_input('press')