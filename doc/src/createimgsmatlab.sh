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

system pdfcrop --margins 10 images/simple_plot_matlab_tocrop.pdf images/simple_plot_matlab.pdf
system pdfcrop --margins 10 images/simple_plot_colours_matlab_tocrop.pdf images/simple_plot_colours_matlab.pdf

system pdfcrop --margins 10 images/default_contour_matlab_tocrop.pdf images/default_contour_matlab.pdf
system pdfcrop --margins 10 images/default_contour3_matlab_tocrop.pdf images/default_contour3_matlab.pdf
system pdfcrop --margins 10 images/contour_imshow_matlab_tocrop.pdf images/contour_imshow_matlab.pdf

system pdfcrop --margins 10 images/contour_10levels_matlab_tocrop.pdf images/contour_10levels_matlab.pdf
system pdfcrop --margins 10 images/contour_10levels_black_matlab_tocrop.pdf images/contour_10levels_black_matlab.pdf
system pdfcrop --margins 10 images/contour_speclevels_matlab_tocrop.pdf images/contour_speclevels_matlab.pdf
system pdfcrop --margins 10 images/contour_clabel_matlab_tocrop.pdf images/contour_clabel_matlab.pdf

system pdfcrop --margins 10 images/quiver_matlab_advanced_tocrop.pdf images/quiver_matlab_advanced.pdf

system doconce combine_images pdf -2 images/simple_plot_matlab images/simple_plot_colours_matlab images/plot_matlab
system doconce combine_images png -2 images/simple_plot_matlab images/simple_plot_colours_matlab images/plot_matlab

system doconce combine_images pdf -2 images/default_contour_matlab images/default_contour3_matlab images/contour_imshow_matlab images/simple_contour_matlab
system doconce combine_images png -2 images/default_contour_matlab images/default_contour3_matlab images/contour_imshow_matlab images/simple_contour_matlab

system doconce combine_images pdf -2 images/contour_10levels_matlab images/contour_10levels_black_matlab images/contour_speclevels_matlab images/contour_clabel_matlab images/advanced_contour_matlab
system doconce combine_images png -2 images/contour_10levels_matlab images/contour_10levels_black_matlab images/contour_speclevels_matlab images/contour_clabel_matlab images/advanced_contour_matlab



