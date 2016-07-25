import numpy as np
from libcpp cimport bool
cimport numpy as np

def k_dom_by_points_cython(p, kValue, points):
    ''' Test whether p can be k-dominated by any point residing in points
    :param p: the point we what to test
    :param kValue: the k value of the k-domination test
    :param points: a set of points that may k-dominate p
    :return: return True if a point in points can k-dominate p otherwise return False
    '''
    isKDom = False
    domSK = points[0]

    for i in range(len(points)):
        isKDom, domSK = k_dom_by_point_cython(p, kValue, points[i])

        if isKDom == True:
            break

    return (isKDom)

def k_dom_by_point_cython(double [:] p, int kValue, double [:] aSkyline):
    ''' Test whether point p is k-dominated by point aSkyline
        return True if p is k-dominated by aSkyline; otherwise false'''
    tmpV = np.subtract(p, aSkyline)

    if np.count_nonzero(tmpV > 0) > 0 and np.count_nonzero(tmpV >= 0) >= kValue:
        return True, aSkyline
    else:
        return False, None

def k_dom_by_point_cython2(double[:] p, int kValue, double[:] aSkyline):
    ''' Test whether point p is k-dominated by point aSkyline
    return True if p is k-dominated by aSkyline; otherwise false'''
    cdef int numWorstDim = 0
    cdef int numQualifyDim = 0
    cdef bint isKDom = False
    cdef object domSK = None
    cdef int len1 = p.shape[0]
    cdef int d
    for d in range(len1):
        if p[d] >= aSkyline[d]:
            numQualifyDim = numQualifyDim + 1
        if p[d] > aSkyline[d]:
            numWorstDim = numWorstDim + 1
        if numQualifyDim >= kValue and numWorstDim > 0:
            isKDom = True
            domSK = aSkyline
            break

    return isKDom, domSK
