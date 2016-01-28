import mayavi.mlab as plt
import os
from math import *
import numpy as np

h0 = 2277.
R = 4.

x = y = np.linspace(-10.,10.,41)
xv, yv = np.meshgrid(x, y, indexing='ij', sparse=False)
hv = h0/(1 + (xv**2+yv**2)/(R**2))

s = np.linspace(0, 2*np.pi, 100)
curve_x = 10*(1 - s/(2*np.pi))*np.cos(s)
curve_y = 10*(1 - s/(2*np.pi))*np.sin(s)
curve_z = h0/(1 + 100*(1 - s/(2*np.pi))**2/(R**2))

# Simple plot of mountain

# Create a figure with white background and black foreground
plt.figure(1, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.mesh(xv, yv, hv, extent=(0,1,0,1,0,1))

# Decorate axes (nb_labels is the number of labels in each direction)
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5,
         color=(0., 0., 0.))

# Decorate the plot with a title (size is the size of the title)
plt.title('h(x,y)', size=0.4)

# Simple plot of mountain and parametric curve
plt.figure(2, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv, extent=(0,1,0,1,0,1), color=(.5, .5, .5))

# Add the parametric curve (tube_radius is the width of the curve)
plt.plot3d(curve_x, curve_y, curve_z, tube_radius=0.2,
           extent=(0,1,0,1,0,1))
plt.axes(xlabel='x', ylabel='y', zlabel='z', nb_labels=5,
         color=(0., 0., 0.))
# endsimpleplots

R2 = 10.
# Create one figure with three subplots
plt.figure(3, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.mesh(xv, yv, hv, extent=(0, 0.25, 0, 0.25, 0, 0.25),
         colormap='cool')
plt.outline(plt.mesh(
    xv, yv, hv,
    extent=(0.375, 0.625, 0, 0.25, 0, 0.25),
    colormap='Accent'))
plt.outline(plt.mesh(
    xv, yv, hv, extent=(0.75, 1, 0, 0.25, 0, 0.25),
    colormap='prism'), color=(.5, .5, .5))
# endsubplot

h0 = 22.77
R = 4.

hv = h0/(1 + (xv**2+yv**2)/(R**2))

# Default contour plot plotted together with surf.
plt.figure(4, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv)

# 10 contour lines (equally spaced contour levels).
plt.figure(5, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.contour_surf(xv, yv, hv, contours=10)

# 10 contour lines (equally spaced contour levels) together with surf.
# Black color for contour lines.
plt.figure(6, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv)
plt.contour_surf(xv, yv, hv, contours=10, color=(0., 0., 0.))

# Specify the contour levels explicitly as a list.
plt.figure(7, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
levels = [5., 10., 15., 20.]
plt.contour_surf(xv, yv, hv, contours=levels)

# View the contours by displaying as an image
plt.figure(8, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.imshow(hv)
#end contourplots


# Define a coarser grid for the vector field
x2 = y2 = np.linspace(-10.,10.,11)
x2v, y2v = np.meshgrid(x2, y2, indexing='ij', sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2)) # Surface on coarse grid
# endcoarsergrid

dhdx, dhdy = np.gradient(h2v)

# Draw contours and normal vector field of h
plt.figure(12, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.contour_surf(xv, yv, hv, contours=20)

# mode controls the style how vectors are drawn
# color controls the colors of the vectors
# scale_factor controls thelength of the vectors
plt.quiver3d(x2v, y2v, h2v, -dhdx, -dhdy, np.ones_like(dhdx),
             mode='arrow', color=(1,0,0), scale_factor=.75)
# end draw contours and normal vector field of h

# Draw surface and normal vector field of h
plt.figure(13, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
plt.surf(xv, yv, hv)
plt.quiver3d(x2v, y2v, h2v, -dhdx, -dhdy, np.ones_like(dhdx),
             mode='arrow', color=(1,0,0), scale_factor=.75)
# end draw surface and normal vector field of h



# Define grid for 3D scalar field
x = y = np.linspace(-10.,10.,41)
z = np.linspace(0,50, 41)
xv, yv, zv = np.meshgrid(x, y, z, sparse=False, indexing='ij')
hv = h0/(1 + (xv**2+yv**2)/(R**2))
gv = zv - hv
# end define grid for 3D scalar field

# Define grid for 3D gradient field
x2 = y2 = np.linspace(-10.,10.,5)
z2 = np.linspace(0, 50, 5)
x2v, y2v, z2v = np.meshgrid(x2, y2, z2, indexing='ij', sparse=False)
h2v = h0/(1 + (x2v**2 + y2v**2)/(R**2))
g2v = z2v - h2v
dhdx, dhdy, dhdz = np.gradient(g2v)
# end define grid for 3D gradient field

# Draw 3D vector field with countours of 3D scalar field
plt.figure(14, fgcolor=(.0, .0, .0), bgcolor=(1.0, 1.0, 1.0))
# opacity controls how contours are visible through each other
plt.contour3d(xv, yv, zv, gv, contours=7, opacity=0.5)
# scale_mode='none' says that the vectors should not be scaled
plt.quiver3d(x2v, y2v, z2v, dhdx, dhdy, dhdz, mode='arrow',\
             scale_mode='none', opacity=0.5)
# end draw 3D vector field with countours of 3D scalar field



# Save figures to files
plt.figure(1)
plt.savefig('images/simple_plot_mayavi.png')

plt.figure(2)
plt.savefig('images/simple_plot_colours_mayavi.png')

plt.figure(3)
plt.savefig('images/subplot.png')

# Save contours plots

plt.figure(4)
plt.savefig('images/simple_contour_mayavi.png')

plt.figure(5)
plt.savefig('images/contour_10levels_mayavi.png')

plt.figure(6)
plt.savefig('images/contour_10levels_black_mayavi.png')

plt.figure(7)
plt.savefig('images/contour_speclevels_mayavi.png')

plt.figure(8)
plt.savefig('images/contour_imshow_mayavi.png')

# Save vector field plots

plt.figure(12)
plt.savefig('images/quiver_contour_mayavi.png')

plt.figure(13)
plt.savefig('images/quiver_surf_mayavi.png')

plt.figure(14)
plt.savefig('images/quiver_mayavi.png')
