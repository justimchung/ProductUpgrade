import numpy as np
import util
from Upgrade_Group import UpgradeGroup
class Upgrade_Algorithm:
    def __init__(self, uGroup, product):
        self.group = uGroup

    def run(self):
        subspace = self.group.getSubspace()

        skyBuffer = self.group.getSkylineBuffer()

        p = self.group.getProduct()

        pMinCost = np.copy(p)

        cost = np.inf

        for dim in range(len(subspace)):

            ptmp = np.copy(p)

            self.group.sortByDim(dim)

            minDimValue = skyBuffer[dim][0]
            ptmp[dim] = minDimValue

            uCost = util.getCost_numpy(pMinCost, p)
            if uCost < cost:
                cost = uCost
                pMinCost = ptmp

            for j in range(len(skyBuffer) - 1):
                si = skyBuffer[j]
                sj = skyBuffer[j + 1]






