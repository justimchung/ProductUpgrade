import unittest
import upgrade_product
import numpy as np

class TestUpgProduct(unittest.TestCase):
    def setUp(self):
        self.p = upgrade_product.upgProduct(np.array([5,6,7], dtype='int32'))
        self.p.setCost(30)

    def test_setCost(self):
        self.p.setCost(40)
        self.assertEqual(40, self.p.getCost())

    def test_getCost(self):
        self.assertEqual(30, self.p.getCost())

if __name__ == '__main__':
    unittest.main()
