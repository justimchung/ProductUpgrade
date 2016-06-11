import numpy as np
import util
from Upgrade_Group import UpgradeGroup
class Upgrade_Algorithm:
    def __init__(self, uGroup):
        self.group = uGroup
        #the dimensionality of the data space
        self.dataspaceDim = len(self.group.getProduct())

    def run(self):
        subspace = self.group.getSubspace()
        pOrigin = self.group.getProduct()
        pMinCost = None
        minCost = np.inf

        for currentDim in np.nditer(subspace):

            self.group.sortByDim(currentDim)

            skyBuffer = self.group.getSkylineBuffer()

            ptmp = self.__upgradeProductInOneDim(currentDim, pOrigin, skyBuffer)

            minCost, pMinCost = self.__determineMinCostProduct(minCost, pOrigin, pMinCost, ptmp)

            for j in range(len(skyBuffer) - 1):
                ptmp = self.__upgradeProductMultipDim(currentDim, j, skyBuffer, subspace)

                minCost, pMinCost = self.__determineMinCostProduct(minCost, pOrigin, pMinCost, ptmp)

        return pMinCost, minCost

    def __upgradeProductMultipDim(self, currentDim, itemIndex, skyBuffer, subspace):
        ptmp2 = np.zeros(self.dataspaceDim)
        si = skyBuffer[itemIndex]
        sj = skyBuffer[itemIndex + 1]
        for k in range(len(subspace)):
            if k == currentDim:
                ptmp2[k] = sj[k] - 1
            else:
                ptmp2[k] = si[k] - 1
        return ptmp2

    def __upgradeProductInOneDim(self, dim, p, skyBuffer):
        ptmp = np.copy(p)
        dimMinValue = skyBuffer[0][dim] - 1
        ptmp[dim] = dimMinValue
        return ptmp

    def __determineMinCostProduct(self, currentMinCost, p, pMinCost, ptmp):
        ugCost = util.getCost_numpy(ptmp, p)
        if ugCost < currentMinCost:
            currentMinCost = ugCost
            pMinCost = ptmp
        return currentMinCost, pMinCost

class New_Upgrade_Algorithm:
    def __init__(self, uGroup, kValue):
        self.upgradeGroup = uGroup
        self.upgAlg = Upgrade_Algorithm(self.upgradeGroup)
        self.upgradeGroup.kValue = kValue






