# -*- coding:utf-8 -*-
# distutils: language = c++
# distutils: sources = Source.cpp
# use python cython_setup.py build_ext --inplace to complier the source code

from libcpp.vector cimport vector
from cython cimport boundscheck, wraparound
cimport numpy as np

cdef extern from "Source.h":
    cdef bint kDomByPoint(vector[int] &p, vector[int] &q, int k)
    cdef bint kDomByPoints(vector[int] &p, vector[vector[int]] &buf, int k)
    cdef vector[vector[int]] retrieveKDomSkyline(vector[vector[int]] &buf, int k)

def kDomByPointPy(p, q, k):
    """
    判斷 p 是否可以被 q k-dom，若可以的話，回傳 true，否則回傳 false
    :param p: 是否可以被 k-dom 的元素
    :param q: 是否可以 k-dom 別人的元素
    :param k: k 值
    :return: 若 q 可以 k-dom p，那回傳 true，否則回傳 false
    """
    return kDomByPoint(p, q, k)

def kDomByPointsPy(p, buf, k):
    """
    p 是否會被 buf 中的某個元素 k-dom
    :param p: 是否可以被 k-dom 的元素
    :param buf: 儲存一群資料的 buffer
    :param k:k 值
    :return: 若 p 被 buf 中的某個元素 k-dom，回傳 true，否則回傳 false
    """
    return kDomByPoints(p, buf, k)

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
