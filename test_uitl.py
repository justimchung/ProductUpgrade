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

    def test_getCostNumPy(self):
        cost = getCost_numpy(np.asarray(self.aSky, dtype='int32'), np.asarray(self.p, dtype='int32'))
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
        iskDom = k_dom_by_point_numpy(np.array(self.p), 3, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 2, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 1, np.array(self.aSky))
        self.assertTrue(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 3, np.array(self.notSky))
        self.assertFalse(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 2, np.array(self.twoDomSky))
        self.assertTrue(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 3, np.array(self.twoDomSky))
        self.assertFalse(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 1, np.array(self.oneDomSky))
        self.assertTrue(iskDom)
        iskDom = k_dom_by_point_numpy(np.array(self.p), 2, np.array(self.oneDomSky))
        self.assertFalse(iskDom)

    def test_k_dom_by_points_numpy(self):
        skylines = np.array([[6, 9, 6], [8, 5, 6], [6, 5, 7]])
        result = k_dom_by_points_numpy(np.array(self.p), 2, skylines)
        self.assertTrue(result)

        result = k_dom_by_points_numpy(np.array([1, 1, 1]), 2, skylines)
        self.assertFalse(result)

        result = k_dom_by_points_numpy(np.array(self.p), 3, skylines)
        self.assertTrue(result)

        result = k_dom_by_points_numpy(np.array([5, 10, 10]), 3, skylines)
        self.assertFalse(result)

    def test_getDominateSubspace_numpy(self):
        r = getDominateSubspace_numpy(self.p, self.aSky)
        self.assertTrue(np.array_equal(r, np.array([0,1,2])))
        r = getDominateSubspace_numpy(self.p, self.notSky)
        self.assertTrue(np.array_equal(r, np.array([])))
        r = getDominateSubspace_numpy(self.p, self.twoDomSky)
        self.assertTrue(np.array_equal(r, np.array([0,1])))
        r = getDominateSubspace_numpy(self.p, self.oneDomSky)
        self.assertTrue(np.array_equal(r, np.array([2])))

    def test_getSubspaceUniqueID_numpy(self):
        test1 = np.array([0,1,2])
        self.assertEqual(getSubspaceUniqueID_numpy(test1), 7)
        test1 = np.array([0])
        self.assertEqual(getSubspaceUniqueID_numpy(test1), 1)
        test1 = np.array([0,1,3,4])
        self.assertEqual(getSubspaceUniqueID_numpy(test1), 27)
        test1 = np.array([])
        self.assertEqual(getSubspaceUniqueID_numpy(test1), 0)

    def test_retrieveSkylinePoints_numpy(self):
        orgData = np.array([[10, 10, 10], [2, 9, 9], [3, 9, 9], [5, 7, 4]])
        sky = retrieveSkylinePoints_numpy(orgData)
        self.assertEqual(2, len(sky))
        self.assertTrue(np.array_equal(np.array([2, 9, 9]), sky[0]))
        self.assertTrue(np.array_equal(np.array([5, 7, 4]), sky[1]))

    def test_cartesian(self):
        result = cartesian(([1, 2, 3], [4, 5], [6, 7]))
        self.assertTrue(np.array_equal(result,
                                       np.array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])))


if __name__ == '__main__':
    unittest.main()