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

system doconce spellcheck -d .dict4spell.txt 3dimplot.do.txt linalg.do.txt


system doconce format pdflatex $name --latex_code_style=vrb-blue1
doconce replace 'section*{Preface}' '' $name.tex
system pdflatex $name
pdflatex $name

system doconce format ipynb plot3d_matplotlib.do.txt -D%s --replace_ref_by_latex_auxno=programming.aux --encoding=utf-8 --allow_refs_to_external_docs
system doconce format matlabnb plot3d_matlabnb.do.txt -D%s --replace_ref_by_latex_auxno=programming.aux --encoding=utf-8 --allow_refs_to_external_docs