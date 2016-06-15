# -*-coding: utf-8 -*-
import numpy as np
import util
from collections import deque
from Upgrade_Group import UpgradeGroup
class Upgrade_Algorithm:
    def __init__(self, uGroup):
        self.group = uGroup
        #the dimensionality of the data space
        self.dataspaceDim = uGroup.getDIM()

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
    def __init__(self, uGroup, kValue, orgP):
        self.upgradeGroup = uGroup
        self.upgAlg = Upgrade_Algorithm(self.upgradeGroup)
        self.kValue = kValue
        self.orgP = orgP
        self.minValBuf = np.full(self.upgradeGroup.getDIM(), np.inf)
        self.dim = uGroup.getDIM()

    def run(self):
        queue = deque()
        skyBuf = self.upgradeGroup.getSkylineBuffer()
        queue.append(self.upgradeGroup)
        while(len(queue) != 0):
            UG = queue.pop()
            upgAlg = Upgrade_Algorithm(UG)
            p, cost = upgAlg.run()
            if util.k_dom_by_points_numpy(p, self.kValue, skyBuf) == True:
                self.__classify_points_by_product(p, UG, queue)
            else:
                self.__modify_minValueBuf(p)


    def __modify_minValueBuf(self, p):
        self.minValBuf = np.minimum(p, self.minValBuf)

    def __classify_points_by_product(self, p, UG, queue):
        """
        依照 p 將 UG 中的每個元素分類，例如分成在 1,2 維度 dominate 一類，
        在 2, 3維度的一類這樣。
        :param p: A product
        :param UG: the upgrade group that will be decomposed
        :param queue: the new upgrade group
        :return:
        """
        dict = {}
        skyBuf = UG.getSkylineBuffer()
        for skyP in skyBuf:
            subSpace = util.getDominateSubspace_numpy(p, skyP)
            id = util.getSubspaceUniqueID_numpy(subSpace)
            if dict.has_key(id):
                dict[id].addSkylinePoint(skyP)
            else:
                dict[id] = UpgradeGroup(self.orgP, subspace=subSpace, size = 25, dim = self.dim)
        for newUG in dict.values():
            queue.append(newUG)


