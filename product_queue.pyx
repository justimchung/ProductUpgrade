# -*- coding:utf-8 -*-
# distutils: language = c++
# distutils: sources = Source.cpp
# use python cython_setup.py build_ext --inplace to complier the source code
import numpy as np
import heapq
from upgrade_product cimport upgProduct
from cython cimport boundscheck, wraparound
cimport numpy as np

DTYPE = np.int
ctypedef np.int_t DTYPE_t

cdef class productQueue:
    """
    This is a minHeap for upgProduct.
    The first element of the queue is an upgProduct with min upgrading cost
    """
    def __init__(self):
        self.data = []

    cdef __push(self, upgProduct p):
        heapq.heappush(self.data, (p.getCost(), p))

    @boundscheck(False)
    @wraparound(False)
    cdef upgProduct __pop(self):
        return heapq.heappop(self.data)[1]

    cpdef int getSize(self):
        return len(self.data)

    def push(self, upgProduct p):
        self.__push(p)

    def pop(self):
        return self.__pop()

    @boundscheck(False)
    @wraparound(False)
    cpdef double getMinCost(self):
        return self.data[0][0]
