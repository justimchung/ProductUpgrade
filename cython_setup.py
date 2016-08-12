# -*- coding:utf-8 -*-
"""
它是用來將 python 的程式碼轉成 cython 所需要的設定檔
"""
# Cython compile instructions

from distutils.core import setup
from Cython.Build import cythonize
import os
import numpy

# Use python cython_setup.py build_ext --inplace
# to compile

setup(
  name = "k_dom_util",
  ext_modules = cythonize('*.pyx'),
  include_dirs=[numpy.get_include(), os.path.join(numpy.get_include(), 'numpy')]
)
