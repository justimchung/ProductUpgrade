import unittest
from upgrade_algorithms import Upgrade_Algorithm
from Upgrade_Group import UpgradeGroup
import numpy as np
from util import *

class TestUpgrade_algorithms(unittest.TestCase):
    def setUp(self):
        self.upG = UpgradeGroup(product = np.array([9, 8]), subspace=np.array([0, 1]), size = 5, dim = 2)
        self.upgradeAlg = Upgrade_Algorithm(self.upG)

    def test_run_upgrade_algorithm(self):
        self.upgradeAlg.run()
        '''after the upgrade algorithm is calling, the "product" cannot be dominated by all the
        products residing in the upG.getSkylineBuffer'''
        skyBuf = self.upG.getSkylineBuffer()
        p = self.upG.getProduct()
        self.assertFalse(k_dom_by_points_numpy(p, 2, skyBuf))


if __name__ == '__main__':
    unittest.main()
