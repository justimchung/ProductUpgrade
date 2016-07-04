# -*- coding:utf-8 -*-
import numpy as np
import util
import Upgrade_Group as ug
import upgrade_algorithms as ualg

class simulator:
    def __init__(self, **kwargs):
        self.rawDataBuffer = np.loadtxt(kwargs['fileName'], delimiter=',')
        self.skyBuffer = self.__retriveSkylines()
        self.kValue = kwargs['kValue']
        self.product = kwargs['product']
        self.dim = len(self.product)
        self.upAlg = self.__initialAlgorithm()

    def __retriveSkylines(self):
        return util.retrieveSkylinePoints_numpy(self.rawDataBuffer)

    def __initialAlgorithm(self):
        aUG = ug.UpgradeGroup(self.product, np.arange(self.dim), size=1000, dim=self.dim)
        aUG.addSkylinePoints(self.skyBuffer)
        upgradeAlg = ualg.Upgrade_Algorithm(aUG)
        return upgradeAlg


    def run(self):
        self.upAlg.run()

