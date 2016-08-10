# -*- coding:utf-8 -*-
import numpy as np
import time

import util
import Upgrade_Group as ug
import upgrade_algorithms as ualg

class simulator:
    def __init__(self, **kwargs):
        self.rawDataBuffer = np.loadtxt(kwargs['fileName'], delimiter=',', dtype='int32')
        self.skyBuffer = self.__retriveSkylines()
        self.kValue = kwargs['kValue']
        self.product = kwargs['product']
        self.algName = kwargs['algName']
        self.dim = len(self.product)
        self.upGroup = self.__initialUpgradeGroup()
        self.upAlg = self.__initialAlgorithm()

    def __retriveSkylines(self):
        return util.retrieveSkylinePoints_numpy(self.rawDataBuffer)

    def __initialUpgradeGroup(self):
        aUG = ug.UpgradeGroup(self.product, np.arange(self.dim), size=1000, dim=self.dim)
        aUG.addSkylinePoints(self.skyBuffer)
        return aUG

    def __initialAlgorithm(self):
        if self.algName == 'Upgrade_Algorithm':
            upgradeAlg = ualg.Upgrade_Algorithm(self.upGroup)
        elif self.algName == 'New_Upgrade_Algorithm':
            upgradeAlg = ualg.New_Upgrade_Algorithm(self.upGroup, self.kValue)
        return upgradeAlg

    def run(self):
        start_time = time.time()
        self.upAlg.run()
        end_time = time.time()
        secs = end_time - start_time
        print(secs)

if __name__ == '__main__':
    sim = simulator(kValue=2, product=np.array([500, 500, 500]), fileName='data_uni_20_3_0.db', algName='Upgrade_Algorithm')
    sim.run()
