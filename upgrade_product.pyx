# -*- coding:utf-8 -*-
# distutils: language = c++
# distutils: sources = Source.cpp
# use python cython_setup.py build_ext --inplace to complier the source code
import numpy as np
from cython cimport boundscheck, wraparound
cimport numpy as np

DTYPE = np.int
ctypedef np.int_t DTYPE_t

cdef class upgProduct:
    """
    The upgraded product class. The class is used in the upgrade algorithm.
    self.attributes is the attribute list of the product
    self.getUpgCost returns the upgrade cost of the product
    """
    def __init__(self, int[::1] attri):
        self.attributes = attri
        self.upgCost = 0.0
    cdef inline __setCost(self, double aCost):
        self.upgCost = aCost
    cdef inline double __getCost(self):
        return self.upgCost
    def setCost(self, cost):
        self.__setCost(cost)
    def getCost(self):
        return self.__getCost()
