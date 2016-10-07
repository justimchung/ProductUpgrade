# -*- coding:utf-8 -*-
# distutils: language = c++
# distutils: sources = Source.cpp
# use python cython_setup.py build_ext --inplace to complier the source code
import numpy as np
import heapq
from cython cimport boundscheck, wraparound
cimport numpy as np
from upgrade_product cimport upgProduct
from product_queue cimport productQueue
import product_queue as pq

DTYPE = np.int
ctypedef np.int_t DTYPE_t

cdef class Upgrade_Algorithm_Cython:
    cdef int dataspaceDim
    cdef int[::1] subspace
    cdef upgProduct originalProduct
    cdef int[:,::1] skyBuffer
    cdef productQueue q

    def __init__(self, uGroup):
        self.group = uGroup
        #the dimensionality of the data space
        self.dataspaceDim = uGroup.getDIM()
        self.subspace = uGroup.getSubspace()
        self.originalProduct = upgProduct(self.group.getProduct().astype(dtype='int32', copy=False))
        self.skyBuffer = None
        self.q = None

    @boundscheck(False)
    @wraparound(False)
    cdef __run(self):
        cdef upgProduct minCostProduct = None
        cdef double minCost = np.inf
        cdef int currentDim = 0
        cdef int N = self.subspace.shape[0]
        cdef upgProduct ptmp = None
        self.q = productQueue()

        for currentDim in range(N):
            self.group.sortByDim(currentDim)
            self.skyBuffer = self.group.getSkylineBuffer().astype(dtype='int32', copy=False)

            ptmp = self.__upgradeProductInOneDim(currentDim)
            if self.q.getMinCost() > ptmp.getCost():
                self.q.push(ptmp)

            self.__upgradeProductUsingMultipleDim(currentDim)



        # for currentDim in np.nditer(subspace):
        #
        #     self.group.sortByDim(currentDim)
        #
        #     skyBuffer = self.group.getSkylineBuffer().astype(dtype='int32', copy=False)
        #
        #     ptmp = self.__upgradeProductInOneDim(currentDim, pOrigin, skyBuffer)
        #
        #     minCost, pMinCost = self.__determineMinCostProduct(minCost, pOrigin, pMinCost, ptmp)
        #
        #     pMinCost = kdom_util.getMinCostProductByUpgradingMultipleDimPy(currentDim, skyBuffer, subspace, pMinCost, pOrigin)
        #
        #     minCost = util.getCost_numpy(np.asarray(pMinCost, dtype='int32'), pOrigin)

        #return np.asarray(pMinCost, dtype='int32'), minCost

    @boundscheck(False)
    @wraparound(False)
    cdef upgProduct __upgradeProductInOneDim(self, int dim):
        cdef upgProduct ptmp = upgProduct(self.originalProduct.attributes)
        ptmp.attributes[dim] = self.skyBuffer[0, dim] - 1
        ptmp.setCost(self.__getCost(self.originalProduct, ptmp))
        return ptmp

    @boundscheck(False)
    @wraparound(False)
    cdef double __getCost(self, upgProduct pOriginal, upgProduct pUpgrade):
        cdef double c = 0.0
        cdef int i = 0
        cdef N = pUpgrade.attributes.shape[0]
        for i in range(N):
           c += (pOriginal.attributes[i] - pUpgrade.attributes[i])
        return c


    @boundscheck(False)
    @wraparound(False)
    cdef __upgradeProductUsingMultipleDim(self, int dim):
        cdef int baseID = 0
        cdef int N = len(self.skyBuffer)
        cdef upgProduct ptmp = None
        cdef int k = 0
        cdef sN = len(self.subspace)
        cdef int aDIM = 0

        for basedID in range(N):
            ptmp = upgProduct(self.skyBuffer[basedID])
            for k in range(sN):
                aDIM = self.subspace[k]
                if aDIM == dim:
                    ptmp.attributes[k] = self.skyBuffer[basedID + 1, k] - 1
                else:
                    ptmp.attributes[k] = self.skyBuffer[basedID, k] - 1

            ptmp.setCost(self.__getCost(self.originalProduct, ptmp))
            if self.q.getMinCost() > ptmp.getCost():
                self.q.push(ptmp)
