#!/bin/bash
set -x

function system {
"$@"
if [ $? -ne 0 ]; then
echo "make.sh: unsuccessful command $@"
echo "abort!"
exit 1
fi
}

system python plot3d_scitools.py
system python plot3d_mayavi.py
system python plot3d_scitools_gnuplot.py --SCITOOLS_easyviz_backend gnuplot
system python plot3d_matplotlib.py

system doconce combine_images pdf -2 images/simple_plot_matplotlib images/simple_plot_colours_matplotlib images/plot_matplotlib
system doconce combine_images png -2 images/simple_plot_matplotlib images/simple_plot_colours_matplotlib images/plot_matplotlib

system doconce combine_images pdf -2 images/default_contour_matplotlib images/default_contour3_matplotlib images/simple_contour_matplotlib
system doconce combine_images png -2 images/default_contour_matplotlib images/default_contour3_matplotlib images/simple_contour_matplotlib

system doconce combine_images pdf -2 images/contour_10levels_matplotlib images/contour_10levels_black_matplotlib images/contour_speclevels_matplotlib images/contour_clabel_matplotlib images/advanced_contour_matplotlib
system doconce combine_images png -2 images/contour_10levels_matplotlib images/contour_10levels_black_matplotlib images/contour_speclevels_matplotlib images/contour_clabel_matplotlib images/advanced_contour_matplotlib

system doconce combine_images pdf -2 images/quiver_matplotlib_advanced images/quiver_matplotlib_simple images/quiver_matplotlib
system doconce combine_images png -2 images/quiver_matplotlib_advanced images/quiver_matplotlib_simple images/quiver_matplotlib




system doconce combine_images png -2 images/simple_plot_scitools images/simple_plot_colours_scitools images/plot_scitools
system doconce combine_images pdf -2 images/simple_plot_scitools images/simple_plot_colours_scitools images/plot_scitools

system doconce combine_images pdf -2 images/default_contour_scitools images/default_contour3_scitools images/simple_contour_scitools
system doconce combine_images png -2 images/default_contour_scitools images/default_contour3_scitools images/simple_contour_scitools

system doconce combine_images pdf -2 images/contour_10levels_scitools images/contour_10levels_black_scitools images/contour_speclevels_scitools images/contour_clabel_scitools images/advanced_contour_scitools
system doconce combine_images png -2 images/contour_10levels_scitools images/contour_10levels_black_scitools images/contour_speclevels_scitools images/contour_clabel_scitools images/advanced_contour_scitools

system doconce combine_images pdf -2 images/quiver_scitools_advanced images/quiver_scitools_simple images/quiver_scitools
system doconce combine_images png -2 images/quiver_scitools_advanced images/quiver_scitools_simple images/quiver_scitools




system doconce combine_images png -2 images/simple_plot_mayavi images/simple_plot_colours_mayavi images/plot_mayavi
system doconce combine_images png -2 images/simple_contour_mayavi images/contour_10levels_mayavi images/contour_10levels_black_mayavi images/contour_speclevels_mayavi images/advanced_contour_mayavi

