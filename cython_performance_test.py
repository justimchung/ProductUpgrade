# -*- coding:utf-8 -*-
import kdom_util
import unittest
import time
import numpy as np
import simulator as sim
import os

"""
這個模組是用來測試不同函式的實作，所造成的效能差異
"""

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.buf = np.array([
            [1, 1, 1, 3, 3, 3],  # 4-dom skyline
            [3, 3, 3, 1, 1, 1],  # 4-dom skyline
            [2, 2, 2, 4, 2, 2],  # 5-dom skyline
            [4, 4, 4, 0, 4, 4],  # 6-dom skyline
            [3, 3, 3, 2, 2, 2]  # nothing
        ])


    def test_k_dom_by_point(self):
        self.assertTrue(kdom_util.kDomByPointPy(self.buf[4], self.buf[1], 6))
        self.assertTrue(kdom_util.kDomByPointPy(self.buf[4], self.buf[1], 5))
        self.assertFalse(kdom_util.kDomByPointPy(self.buf[0], self.buf[0], 5))
        self.assertFalse(kdom_util.kDomByPointPy(self.buf[0], self.buf[1], 5))
        self.assertFalse(kdom_util.kDomByPointPy(self.buf[1], self.buf[1], 5))
        self.assertFalse(kdom_util.kDomByPointPy(self.buf[1], self.buf[0], 5))

    def test_k_dom_by_points(self):
        self.assertTrue(kdom_util.kDomByPointsPy(self.buf[4], self.buf, 5))
        self.assertTrue(kdom_util.kDomByPointsPy(self.buf[4], self.buf, 6))
        self.assertTrue(kdom_util.kDomByPointsPy(self.buf[4], self.buf, 4))
        self.assertTrue(kdom_util.kDomByPointsPy(self.buf[0], self.buf, 3))
        self.assertFalse(kdom_util.kDomByPointsPy(self.buf[0], self.buf, 6))
        self.assertFalse(kdom_util.kDomByPointsPy(self.buf[0], self.buf, 5))
        self.assertFalse(kdom_util.kDomByPointsPy(self.buf[3], self.buf, 6))
        self.assertTrue(kdom_util.kDomByPointsPy(self.buf[3], self.buf, 5))

    def test_retrieve_KSkylines(self):
        kdomSky = kdom_util.retrieveKDomSkylinePy(self.buf, 4)
        self.assertEqual(2, len(kdomSky))
        self.assertTrue(np.array_equal(np.array([[1,1,1,3,3,3], [3,3,3,1,1,1]]), kdomSky))
        kdomSky = kdom_util.retrieveKDomSkylinePy(self.buf, 5)
        self.assertEqual(3, len(kdomSky))
        self.assertTrue(np.array_equal(np.array([[1,1,1,3,3,3], [3,3,3,1,1,1],[2,2,2,4,2,2]]), kdomSky))



if __name__ == '__main__':
    #unittest.main()
    pathName = os.path.dirname(os.path.abspath(__file__))
    ProductBuffer = np.loadtxt(pathName + "\data\product_uni_1_5_0.db", delimiter=",")
    aSim = sim.simulator(kValue=4, fileName=os.path.dirname(os.path.abspath(__file__)) + '\data\data_corr_100_5_0.db',
                         algName='Upgrade_Algorithm',
                         product=ProductBuffer[0])
    start_time = time.time()
    aSim.run()
    end_time = time.time()
    print(end_time-start_time)
