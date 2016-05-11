import unittest
from util import *


class TestUtil(unittest.TestCase):
    def setUp(self):
        self.p = [10, 8, 9]
        self.aSky = [8, 7, 6]  #aSky 3-dominate p
        self.notSky = [11, 12, 13] #notSky does not dominate p
        self.twoDomSky = [9,7,10]  #twoDomSky 2-dominate p
        self.oneDomSky = [11, 9, 8] # oneDomSky 1-dominate p
    def test_k_dom_by_point(self):
        iskDom, sk = k_dom_by_point(self.p, 3, self.aSky)
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 2, self.aSky)
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 1, self.aSky)
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 3, self.notSky)
        self.assertFalse(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 2, self.twoDomSky)
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 3, self.twoDomSky)
        self.assertFalse(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 1, self.oneDomSky)
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point(self.p, 2, self.oneDomSky)
        self.assertFalse(iskDom)
    def test_getCost(self):
        cost = getCost(self.aSky, self.p)
        self.assertEqual(cost, 6)



if __name__ == '__main__':
    unittest.main()


