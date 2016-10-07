# -*- coding:utf-8 -*-
# distutils: language = c++
# distutils: sources = Source.cpp
# use python cython_setup.py build_ext --inplace to complier the source code
import numpy as np
from libcpp.vector cimport vector
from cython cimport boundscheck, wraparound
cimport numpy as np

DTYPE = np.int
ctypedef np.int_t DTYPE_t


@boundscheck(False)
@wraparound(False)
cdef bint kDomByPointCython(int[::1] p, int[::1] q, int k):
    cdef int len = p.shape[0]
    cdef int i = 0
    cdef int numWorstDim = 0
    cdef int numQualifyDim = 0
    cdef bint isKDom = False
    for i in range(len):
        if p[i] >= q[i]:
            numQualifyDim=numQualifyDim+1
        if p[i] > q[i]:
            numWorstDim=numWorstDim+1
        if (numQualifyDim >= k) and (numWorstDim >0):
            isKDom = True
            break
    return isKDom


@boundscheck(False)
@wraparound(False)
cdef bint kDomByPointsCython(int[::1] p, int[:,::1] buf, int k):
    cdef int len = buf.shape[0]
    cdef int i = 0
    for i in range(len):
        if kDomByPointCython(p, buf[i], k) == True:
            return True
    return False

cdef int[::1] getMinCostProductUsingMultipleDimCython(int currentDIM, int[:,::1] skyBuf, int[::1] subspace,  int[::1] minCostProduct, int[::1] originalProduct):
    cdef int N = skyBuf.shape[0]
    cdef int i = 0
    cdef minCost = getCostPy(minCostProduct, originalProduct)

cdef upgradeProductMultipleDim(int currentDIM, int basedID, int[:,::1] skyBuf, int[::1] subspace):
    cdef int[::1] aProduct = np.empty()


cdef extern from "Source.h":
    cdef bint kDomByPoint(vector[int] &p, vector[int] &q, int k)
    cdef bint kDomByPoints(vector[int] &p, vector[vector[int]] &buf, int k)
    cdef vector[vector[int]] retrieveKDomSkyline(vector[vector[int]] &buf, int k)
    cdef vector[int] getMinCostProductUsingMultipleDim(int currentDIM, vector[vector[int]] &skyBuf, vector[int] &subspace, vector[int] &minCostProduct, vector[int] &origionalProduct)

def kDomByPointPy(p, q, k):
    """
    判斷 p 是否可以被 q k-dom，若可以的話，回傳 true，否則回傳 false
    :param p: 是否可以被 k-dom 的元素
    :param q: 是否可以 k-dom 別人的元素
    :param k: k 值
    :return: 若 q 可以 k-dom p，那回傳 true，否則回傳 false
    """
    return kDomByPointCython(p, q, k)

def kDomByPointsPy(p, buf, k):
    """
    p 是否會被 buf 中的某個元素 k-dom
    :param p: 是否可以被 k-dom 的元素
    :param buf: 儲存一群資料的 buffer
    :param k:k 值
    :return: 若 p 被 buf 中的某個元素 k-dom，回傳 true，否則回傳 false
    """
    return kDomByPointsCython(p, buf, k)

def retrieveKDomSkylinePy(buf, k):
    """
    Return a set of k-dominant skyline from buf
    :param buf: 一群資料點的集合
    :param k: k value
    :return: 由 buf 中過濾出 k-dom skyline，並回傳
    """
    return retrieveKDomSkyline(buf, k)

@boundscheck(False)
@wraparound(False)
def getCostPy(int[::1] pUpgrade, int[::1] pOriginal):
    cdef:
        int k = 0
        int N = pUpgrade.shape[0]
        int cost = 0
    for k in range(N):
        cost += (pOriginal[k] - pUpgrade[k])
    return cost


@boundscheck(False)
@wraparound(False)
def upgradeProductMultipleDimPy(int currentDim, int itemIndex, int[:,::1] skyBuf, int[::1] subspace, int[::1] upgradeProduct):
    cdef:
        int k = 0
        int N = subspace.shape[0]
    for k in range(N):
        if k == currentDim:
            upgradeProduct[k] = skyBuf[itemIndex + 1, k] - 1
        else:
            upgradeProduct[k]= skyBuf[itemIndex, k] - 1

def getMinCostProductByUpgradingMultipleDimPy(currentDIM, skyBuf, subspace, minCostProduct, origionalProduct):
    return getMinCostProductUsingMultipleDim(currentDIM, skyBuf, subspace, minCostProduct, origionalProduct)

