#!/bin/bash

function system {
"$@"
if [ $? -ne 0 ]; then
echo "make.sh: unsuccessful command $@"
echo "abort!"
exit 1
fi
}


system doconce combine_images pdf -2 images/simpleplotmatplotlib images/simpleplotcoloursmatplotlib images/plotmatplotlib
system doconce combine_images png -2 images/simpleplotmatplotlib images/simpleplotcoloursmatplotlib images/plotmatplotlib

system doconce combine_images pdf -2 images/contour10levelsmatplotlib images/contour10levelsblackmatplotlib images/contourspeclevelsmatplotlib images/contourclabelmatplotlib images/advancedcontourmatplotlib
system doconce combine_images png -2 images/contour10levelsmatplotlib images/contour10levelsblackmatplotlib images/contourspeclevelsmatplotlib images/contourclabelmatplotlib images/advancedcontourmatplotlib

system doconce combine_images pdf -2 images/quivermatplotlibsimple images/quivermatplotlibadvanced images/quivermatplotlib
system doconce combine_images png -2 images/quivermatplotlibsimple images/quivermatplotlibadvanced images/quivermatplotlib




system doconce combine_images png -2 images/simpleplotscitools images/simpleplotcoloursscitools images/plotscitools

system doconce combine_images pdf -2 images/contour10levelsscitools images/contour10levelsblackscitools images/contourspeclevelsscitools images/contourclabelscitools images/advancedcontourscitools
system doconce combine_images png -2 images/contour10levelsscitools images/contour10levelsblackscitools images/contourspeclevelsscitools images/contourclabelscitools images/advancedcontourscitools

system doconce combine_images pdf -2 images/quiverscitoolssimple images/quiverscitoolsadvanced images/quiverscitools
system doconce combine_images png -2 images/quiverscitoolssimple images/quiverscitoolsadvanced images/quiverscitools




system doconce combine_images png -2 images/simpleplotmayavi images/simpleplotcoloursmayavi images/plotmayavi
system doconce combine_images png -2 images/simplecontourmayavi images/contour10levelsmayavi images/contour10levelsblackmayavi images/contourspeclevelsmayavi images/advancedcontourmayavi

