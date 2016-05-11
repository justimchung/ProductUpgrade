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

def getCost(pUpgrade, pOriginal):
    '''Return the upgrade cost for upgrading pOriginal to pUpgrade'''
    cost = 0
    for i in range(len(pUpgrade)):
        cost += (pOriginal[i] - pUpgrade[i])
    return cost

