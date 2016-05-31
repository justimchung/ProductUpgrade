import numpy as np
import util
from Upgrade_Group import UpgradeGroup
class Upgrade_Algorithm:
    def __init__(self, uGroup):
        self.group = uGroup

    def run(self):
        subspace = self.group.getSubspace()

        p = self.group.getProduct()

        pMinCost = np.copy(p)

        cost = np.inf

        for dim in range(len(subspace)):

            ptmp = np.copy(p)

            self.group.sortByDim(dim)

            skyBuffer = self.group.getSkylineBuffer()

            dimMinValue = skyBuffer[0][dim] - 1
            ptmp[dim] = dimMinValue

            ugCost = util.getCost_numpy(ptmp, p)
            if ugCost < cost:
                cost = ugCost
                pMinCost = ptmp

            ptmp2 = np.copy(p)

            for j in range(len(skyBuffer) - 1):
                si = skyBuffer[j]
                sj = skyBuffer[j + 1]

                for k in range(len(subspace)):
                    if k == dim:
                        ptmp2[k] = sj[k] - 1
                    else:
                        ptmp2[k] = si[k] - 1

                ugCost = util.getCost_numpy(ptmp2, p)
                if ugCost < cost:
                    cost = ugCost
                    pMinCost = ptmp2

        return pMinCost, cost







