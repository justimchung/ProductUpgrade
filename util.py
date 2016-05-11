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

