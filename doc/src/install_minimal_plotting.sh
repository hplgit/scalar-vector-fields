#!/bin/bash
# Automatically generated script by
# vagrantbox/doc/src/vagrant/src-vagrant/deb2sh.py
# where vagrantbox is the directory arising from
# git clone git@github.com:hplgit/vagrantbox.git

# The script is based on packages listed in debpkg_minimal.txt.

set -x  # make sure each command is printed in the terminal

function apt_install {
  sudo apt-get -y install $1
  if [ $? -ne 0 ]; then
    echo "could not install $1 - abort"
    exit 1
  fi
}

function pip_install {
  sudo pip install --upgrade "$@"
  if [ $? -ne 0 ]; then
    echo "could not install $p - abort"
    exit 1
  fi
}

sudo apt-get update --fix-missing

# Minimal installation for a Python ecosystem
# for scientific computing

# Install downloaded source code in ~/srclib
# cd
if [ ! -d srclib ]; then mkdir srclib; fi

# Editors
apt_install emacs
apt_install python-mode
apt_install gedit
apt_install vim
apt_install ispell

# Compilers
apt_install gcc
apt_install g++
apt_install gawk
apt_install f2c
apt_install gfortran
apt_install autoconf
apt_install automake
apt_install autotools-dev

# Numerical libraries
apt_install libatlas-base-dev
apt_install libsuitesparse-dev

# Version control systems
apt_install subversion
apt_install mercurial
apt_install cvs
apt_install git
apt_install gitk
apt_install bzr

# Python
apt_install idle
apt_install python-pip
apt_install python-setuptools
apt_install python-dev
# Matplotlib requires libfreetype-dev libpng-dev
# (otherwise pip install matplotlib does not work)
apt_install libfreetype6-dev
apt_install libpng-dev
pip_install numpy
pip_install sympy
pip_install cython
apt_install swig
#pip install pyparsing
#pip install matplotlib
apt_install python-matplotlib
pip_install scipy
#ipython-notebook  # too old version in debian
pip_install ipython --upgrade
pip_install tornado --upgrade
pip_install pyzmq --upgrade
pip_install nose
pip_install pytest
pip_install sphinx
apt_install pydb
apt_install python-profiler
apt_install python-dev
apt_install spyder

# Gnuplot
apt_install gnuplot
apt_install gnuplot-doc
apt_install gnuplot-qt
apt_install python-gnuplot
apt_install liblualib50-dev
#gnuplot-x11


# Image manipulation
apt_install imagemagick
apt_install netpbm
apt_install mjpegtools
apt_install pdftk
apt_install giftrans
apt_install gv
apt_install evince
apt_install smpeg-plaympeg
apt_install mplayer
apt_install totem


# Support for Norwegian
apt_install language-pack-nb-base

pip_install -e git+https://github.com/hplgit/scitools.git#egg=scitools

pip_install mayavi --upgrade
# Does not work: pip install -e hg+https://bitbucket.org/khinsen/scientificpython#egg=scientificpython
# Do manual install instead
cd srclib
hg clone https://bitbucket.org/khinsen/scientificpython
cd scientificpython
sudo python setup.py install
cd ../..
echo "Everything is successfully installed!"
