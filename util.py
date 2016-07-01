import numpy as np

def k_dom_by_point_numpy(p, kValue, aSkyline):
    ''' Test whether point p is k-dominated by point aSkyline
        return True if p is k-dominated by aSkyline; otherwise false'''
    tmpV = np.subtract(p, aSkyline)

    if np.count_nonzero(tmpV > 0) > 0 and np.count_nonzero(tmpV >= 0) >= kValue:
        return True, aSkyline
    else:
        return False, None

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

    return np.sum(np.subtract(pOriginal, pUpgrade))

def getDominateSubspace_numpy(p, psky):
    '''Return a list A which indicate the subspace that psky is superial over p.'''
    l = []
    for i in range(len(p)):
        if p[i] > psky[i]:
            l.append(i)
    return l


def getSubspaceUniqueID_numpy(subspace):
    """
    Given a subspace return an unique id of the subspace
    :param subspace: the subspace to be determined the unique id
    :return: the unique id of the subspace
    """
    uid = 0
    for i in range(len(subspace)):
        uid +=  2**(subspace[i])
    return uid

def retrieveSkylinePoints_numpy(orgData):
    """
    Given a set of raw data, retrieve the skyline points from the raw data.
    :param orgData: the raw data set
    :return: a set of skyline points from orgData
    """
    sky = []
    dim = len(orgData[0])

    for i in range(len(orgData)):
        p = orgData[i]
        if not k_dom_by_points_numpy(p, dim, orgData):
            sky.append(p)
    return sky


def k_dom_by_points_numpy(p, kValue, points):
    ''' Test whether p can be k-dominated by any point residing in points
    :param p: the point we what to test
    :param kValue: the k value of the k-domination test
    :param points: a set of points that may k-dominate p
    :return: return True if a point in points can k-dominate p otherwise return False
    '''
    isKDom = False
    domSK = points[0]

    for i in range(len(points)):
        isKDom, domSK = k_dom_by_point_numpy(p, kValue, points[i])

        if isKDom == True:
            break

    return (isKDom)



