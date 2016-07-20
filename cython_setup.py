# -*- coding:utf-8 -*-
"""
它是用來將 python 的程式碼轉成 cython 所需要的設定檔
"""
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy

setup(
    cmdclass = {'build_ext': build_ext},
    package_dir = {"ProductUpgrade": "."},
    ext_modules = cythonize("kdom_util.pyx"), include_dirs=[numpy.get_include()]
)
