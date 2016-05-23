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

    def test_k_dom_by_points(self):
        skylines = [[6,9,6],[8,5,6],[6,5,7]]
        result = k_dom_by_points(self.p, 2, skylines)
        self.assertTrue(result)

        result = k_dom_by_points([1,1,1], 2, skylines)
        self.assertFalse(result)

        result = k_dom_by_points(self.p, 3, skylines)
        self.assertTrue(result)

        result = k_dom_by_points([5, 10, 10], 3, skylines)
        self.assertFalse(result)

    def test_k_dom_by_point_numpy(self):
        iskDom, sk = k_dom_by_point_numpy(self.p, 3, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 2, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 1, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 3, np.array(self.notSky))
        self.assertFalse(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 2, np.array(self.twoDomSky))
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 3, np.array(self.twoDomSky))
        self.assertFalse(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 1, np.array(self.oneDomSky))
        self.assertTrue(iskDom)
        iskDom, sk = k_dom_by_point_numpy(self.p, 2, np.array(self.oneDomSky))
        self.assertFalse(iskDom)

    def test_k_dom_by_points_numpy(self):
        skylines = np.array([[6, 9, 6], [8, 5, 6], [6, 5, 7]])
        result = k_dom_by_points_numpy(self.p, 2, skylines)
        self.assertTrue(result)

        result = k_dom_by_points_numpy([1, 1, 1], 2, skylines)
        self.assertFalse(result)

        result = k_dom_by_points_numpy(self.p, 3, skylines)
        self.assertTrue(result)

        result = k_dom_by_points_numpy([5, 10, 10], 3, skylines)
        self.assertFalse(result)

    def test_getDominateSubspace_numpy(self):
        r = getDominateSubspace_numpy(self.p, self.aSky)
        self.assertTrue(np.array_equal(r, np.array([1,1,1])))
        r = getDominateSubspace_numpy(self.p, self.notSky)
        self.assertTrue(np.array_equal(r, np.array([0,0,0])))
        r = getDominateSubspace_numpy(self.p, self.twoDomSky)
        self.assertTrue(np.array_equal(r, np.array([1,1,0])))
        r = getDominateSubspace_numpy(self.p, self.oneDomSky)
        self.assertTrue(np.array_equal(r, np.array([0,0,1])))




if __name__ == '__main__':
    unittest.main()


