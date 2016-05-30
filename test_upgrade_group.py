import numpy as np
import unittest
from Upgrade_Group import UpgradeGroup

class TestUpgradeGroup(unittest.TestCase):
    def setUp(self):
        self.UpgradeGroup = UpgradeGroup(product = np.array([9, 8]), subspace= np.array([0,1]), size = 2, dim=2)



    def test_getproduct(self):
        p = self.UpgradeGroup.getProduct()
        self.assertTrue(np.array_equal(p, np.array([9,8])))

    def test_addSkylinePoint(self):
        self.UpgradeGroup.addSkylinePoint(np.array([4,5]))
        self.UpgradeGroup.addSkylinePoint(np.array([7,5]))
        skyBuf = self.UpgradeGroup.getSkylineBuffer()
        self.assertEqual(2, len(skyBuf))
        self.assertTrue(np.array_equal(skyBuf[0], np.array([4,5])))
        self.assertTrue(np.array_equal(skyBuf[1], np.array([7,5])))

    def test_sortByDim(self):
        self.UpgradeGroup.addSkylinePoint(np.array([4,6]))
        self.UpgradeGroup.addSkylinePoint(np.array([7,5]))
        self.UpgradeGroup.sortByDim(1)
        self.assertEqual(5, self.UpgradeGroup.getSkylineBuffer()[0][1])
        self.assertEqual(6, self.UpgradeGroup.getSkylineBuffer()[1][1])

    def test_getSubSpace(self):
        subSpace = self.UpgradeGroup.getSubspace()
        self.assertTrue(np.array_equal(subSpace, np.array([0,1])))

if __name__ == '__main__':
    unittest.main()
