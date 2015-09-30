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
system doconce formt pdflatex $name --latex_code_style=lst-blue1
system pdflatex $name
pdflatex $name
