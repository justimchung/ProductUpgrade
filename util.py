import numpy as np
import kdom_util

def k_dom_by_point_numpy(p, kValue, aSkyline):
    ''' Test whether point p is k-dominated by point aSkyline
        return True if p is k-dominated by aSkyline; otherwise false'''

    return kdom_util.kDomByPointPy(p, aSkyline, kValue)

def k_dom_by_point(p, kValue, aSkyline):
    ''' Test whether point p is k-dominated by point aSkyline
    return True if p is k-dominated by aSkyline; otherwise false'''
    numWorstDim = 0
    numQualifyDim = 0
    isKDom = False
    domSK = None
    for d in range(len(p)):
        if p[d] >= aSkyline[d]:
            numQualifyDim = numQualifyDim + 1
        if p[d] > aSkyline[d]:
            numWorstDim = numWorstDim + 1
        if numQualifyDim >= kValue and numWorstDim > 0:
            isKDom = True
            domSK = aSkyline
            break

    return isKDom, domSK


def k_dom_by_points(p, kValue, points):
    ''' Test whether p can be k-dominated by any point residing in points
    :param p: the point we what to test
    :param kValue: the k value of the k-domination test
    :param points: a set of points that may k-dominate p
    :return: return True if a point in points can k-dominate p otherwise return False
    '''
    isKDom = False
    domSK = points[0]

    for sk in points:
        isKDom, domSK = k_dom_by_point(p, kValue, sk)

        if isKDom == True:
            break

    return (isKDom)

def getCost(pUpgrade, pOriginal):
    '''Return the upgrade cost for upgrading pOriginal to pUpgrade'''
    cost = 0
    for i in range(len(pUpgrade)):
        cost += (pOriginal[i] - pUpgrade[i])
    return cost

def getCost_numpy(pUpgrade, pOriginal):
    '''Return the upgrade cost for upgrading pOriginal to pUpgrade'''

    return kdom_util.getCostPy(pUpgrade, pOriginal)

def getDominateSubspace_numpy(p, psky):
    '''Return a list A which indicate the subspace that psky is superial over p.'''
    l = []
    for i in range(len(p)):
        if p[i] > psky[i]:
            l.append(i)
    return np.asarray(l, dtype='int32')


def getSubspaceUniqueID_numpy(subspace):
    """
    Given a subspace return an unique id of the subspace
    :param subspace: the subspace to be determined the unique id
    :return: the unique id of the subspace
    """
    if len(subspace) == 0:
        return 0
    uid = 0
    for i in range(len(subspace)):
        uid += 2 ** subspace[i]
    return uid

def retrieveSkylinePoints_numpy(orgData):
    """
    Given a set of raw data, retrieve the skyline points from the raw data.
    :param orgData: the raw data set
    :return: a set of skyline points from orgData
    """
    dim = len(orgData[0])
    return kdom_util.retrieveKDomSkylinePy(orgData, dim)

def k_dom_by_points_numpy(p, kValue, points):
    ''' Test whether p can be k-dominated by any point residing in points
    :param p: the point we what to test
    :param kValue: the k value of the k-domination test
    :param points: a set of points that may k-dominate p
    :return: return True if a point in points can k-dominate p otherwise return False
    '''
    return kdom_util.kDomByPointsPy(p, points, kValue)

def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = n / arrays[0].size
    out[:, 0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]
    return out



