# -*-coding: utf-8 -*-
import unittest
from upgrade_algorithms import Upgrade_Algorithm
from upgrade_algorithms import New_Upgrade_Algorithm
from Upgrade_Group import UpgradeGroup
import numpy as np
from util import *

class TestUpgrade_algorithms(unittest.TestCase):

    def test_run_upgrade_algorithm_for_full_skyline(self):
        self.upG = UpgradeGroup(product = np.array([9, 8]), subspace=np.array([0, 1]), size = 5, dim = 2)
        self.upG.addSkylinePoint(np.array([7, 8]))
        self.upG.addSkylinePoint(np.array([8, 6]))
        self.upgradeAlg = Upgrade_Algorithm(self.upG)
        p, minCost = self.upgradeAlg.run()
        '''after the upgrade algorithm is calling, the "product" cannot be dominated by all the
        products residing in the upG.getSkylineBuffer'''
        skyBuf = self.upG.getSkylineBuffer()
        self.assertFalse(k_dom_by_points_numpy(p, 2, skyBuf))
        self.assertEqual(3, minCost)

    def test_run_upgrade_alg_for_one_dominantsky(self):
        """
        test_run_upgrade_alg_for_one_dominantsky test whether the upgrade algorithm can
        work well in 1-dominant skyline scenario
        """
        self.upG = UpgradeGroup(product = np.array([6, 8]), subspace=np.array([1]), size = 5, dim = 2)
        self.upG.addSkylinePoint(np.array([8, 6]))
        self.upgradeAlg = Upgrade_Algorithm(self.upG)
        p, minCost = self.upgradeAlg.run()
        skyBuf = self.upG.getSkylineBuffer()
        self.assertFalse(k_dom_by_points_numpy(p, 1, skyBuf))
        self.assertEqual(3, minCost)

    def test_run_new_upgrade_algorithm_for_full_skyline(self):
        """
        測試 new upgrade algorithm，測看看它能不能在 k = 2 以及 dim = 2 的情況下，成功地把產品升
        級成 skyline product
        :return: none
        """
        self.upG = UpgradeGroup(product = np.array([9, 8]), subspace=np.array([0, 1]), size = 5, dim = 2)
        self.upG.addSkylinePoint(np.array([7, 8]))
        self.upG.addSkylinePoint(np.array([8, 6]))
        newUpGradeAlg = New_Upgrade_Algorithm(self.upG, 2, self.upG.getProduct())
        p, minCost = newUpGradeAlg.run()
        skyBuf = self.upG.getSkylineBuffer()
        self.assertFalse(k_dom_by_points_numpy(p, 2, skyBuf))
        self.assertEqual(3, minCost)

    def test_run_new_upgrade_algorithm_for_one_dominant_skyline(self):
        """
        測試 new upgrade algorithm，測看看它能不能在 k = 1 以及 dim = 2 的情況下，成功地把產品升
        級成 1-dominant skyline product
        :return: none
        """
        k_value = 1
        self.upG = UpgradeGroup(product = np.array([9, 8]), subspace=np.array([0, 1]), size = 5, dim = 2)
        self.upG.addSkylinePoint(np.array([7, 8]))
        self.upG.addSkylinePoint(np.array([8, 6]))
        newUpGradeAlg = New_Upgrade_Algorithm(self.upG, k_value, self.upG.getProduct())
        p, minCost = newUpGradeAlg.run()
        skyBuf = self.upG.getSkylineBuffer()
        self.assertFalse(k_dom_by_points_numpy(p, k_value, skyBuf))
        self.assertEqual(5, minCost)
if __name__ == '__main__':
    unittest.main()
