# -*-coding: utf-8 -*-
import numpy as np
import util
import kdom_util
from collections import deque
from Upgrade_Group import UpgradeGroup


class Upgrade_Algorithm:
    def __init__(self, uGroup):
        self.group = uGroup
        #the dimensionality of the data space
        self.dataspaceDim = uGroup.getDIM()

    def run(self):
        subspace = self.group.getSubspace()
        pOrigin = self.group.getProduct().astype(dtype='int32', copy=False)
        pMinCost = None
        minCost = np.inf

        for currentDim in np.nditer(subspace):

            self.group.sortByDim(currentDim)

            skyBuffer = self.group.getSkylineBuffer().astype(dtype='int32', copy=False)

            ptmp = self.__upgradeProductInOneDim(currentDim, pOrigin, skyBuffer)

            minCost, pMinCost = self.__determineMinCostProduct(minCost, pOrigin, pMinCost, ptmp)

            pMinCost = kdom_util.getMinCostProductByUpgradingMultipleDimPy(currentDim, skyBuffer, subspace, pMinCost, pOrigin)

            minCost = util.getCost_numpy(np.asarray(pMinCost, dtype='int32'), pOrigin)

        return np.asarray(pMinCost, dtype='int32'), minCost

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
        self.kValue = kValue
        self.orgP = uGroup.getProduct()
        self.minValBuf = np.full(self.upgradeGroup.getDIM(), np.inf)
        self.dim = uGroup.getDIM()
    def run(self):
        queue = deque()
        skyBuf = self.upgradeGroup.getSkylineBuffer()
        queue.append(self.upgradeGroup)
        while len(queue) != 0:
            UG = queue.pop()
            upgAlg = Upgrade_Algorithm(UG)
            p, cost = upgAlg.run()
            if util.k_dom_by_points_numpy(p, self.kValue, skyBuf):
                self.__classify_points_by_product(p, UG, queue)
            else:
                self.__modify_minValueBuf(p)

        minCost = util.getCost_numpy(self.minValBuf.astype(dtype='int32', copy=False), np.asarray(self.orgP, dtype='int32'))
        return self.minValBuf, minCost


    def __modify_minValueBuf(self, p):
        self.minValBuf = np.minimum(p, self.minValBuf)

    def __classify_points_by_product(self, p, UG, queue):
        """
        依照 p 將 UG 中的每個元素分類，例如分成在 1,2 維度 dominate 一類，
        在 2, 3維度的一類這樣。分類完的upgrade group要放入 queue 中。
        :param p: A product
        :param UG: the upgrade group that will be decomposed
        :param queue: the new upgrade group
        :return:
        """
        dict = {}
        skyBuf = UG.getSkylineBuffer()
        for skyP in skyBuf:
            isKDom = util.k_dom_by_point_numpy(p, self.kValue, skyP)
            if not isKDom:
                continue
            subSpace = util.getDominateSubspace_numpy(p, skyP)
            id = util.getSubspaceUniqueID_numpy(subSpace)
            if id in dict:
                dict[id].addSkylinePoint(skyP)
            else:
                newUG = UpgradeGroup(p, subspace=subSpace, size = 25, dim = self.dim)
                newUG.addSkylinePoint(skyP)
                dict[id] = newUG

        for newUG in dict.values():
            queue.append(newUG)


