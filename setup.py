#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy
import os

torch_home = os.environ['TORCH_HOME']
include_dir = os.path.join(torch_home, 'install', 'include')
library_dir = os.path.join(torch_home, 'install', 'lib')

setup(
  name="python2torch",
  version="0.1",
  description="Call torch functions from python.",
  author="Kevin Matzen",
  url="https://github.com/kmatzen/python2torch",
  cmdclass = {'build_ext': build_ext},
  ext_modules = [
    Extension("python2torch",
              sources=["python2torch.pyx"],
              include_dirs=[numpy.get_include(), include_dir],
              library_dirs=[library_dir],
              libraries = ['TH', 'luaT', 'luajit'])
  ]
)
