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

name=programming
namematlab=programmingmatlab

system doconce spellcheck -d .dict4spell.txt 3dimplot.do.txt linalg.do.txt

system doconce format pdflatex $name --latex_code_style=vrb-blue1 MATLAB_TOO=False --encoding=utf-8
doconce replace 'section*{Preface}' '' $name.tex
system pdflatex $name
system pdflatex $name

system doconce format pdflatex $name --latex_code_style=vrb-blue1 MATLAB_TOO=True --encoding=utf-8
cp $name.tex $namematlab.tex
doconce replace 'section*{Preface}' '' $namematlab.tex
mv $name.tex $namematlab.tex
system pdflatex $namematlab
system pdflatex $namematlab

system doconce format ipynb plot3d_matplotlib.do.txt  --replace_ref_by_latex_auxno=$name.aux --encoding=utf-8 --allow_refs_to_external_docs
system doconce format matlabnb plot3d_matlabnb.do.txt --replace_ref_by_latex_auxno=$namematlab.aux --encoding=utf-8 --allow_refs_to_external_docs
