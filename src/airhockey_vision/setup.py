#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['airhockey_vision'],
    package_dir={'': 'src'},
    install_requires=['opencv-contrib-python', 'apriltags', 'imutils']
)

setup(**setup_args)
