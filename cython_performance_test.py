# -*- coding:utf-8 -*-
import kdom_util_cython
import time
import numpy as np
import os
import util
"""
這個模組是用來測試不同函式的實作，所造成的效能差異
"""

def calc_pure_python_performance(pointBuffer, point, kValue):
    start_time = time.time()
    for skyp in pointBuffer:
        kdom_util_cython.k_dom_by_point_cython(point, kValue, skyp)
    end_time = time.time()
    secs = end_time - start_time
    print(secs)


def calc_pure_python_performance2(pointBuffer, point, kValue):
    start_time = time.time()
    for skyp in pointBuffer:
        kdom_util_cython.k_dom_by_point_cython2(point, kValue, skyp)
    end_time = time.time()
    secs = end_time - start_time
    print(secs)

def calc_pure_python_kdombypoints_performance(pointBuffer, kValue):
    start_time = time.time()
    for p in pointBuffer:
        util.k_dom_by_points_numpy(p, kValue, pointBuffer)
    end_time = time.time()
    secs = end_time - start_time
    print(secs)

def calc_cpython_kdombypoints_performance(pointBuffer, kValue):
    start_time = time.time()
    for p in pointBuffer:
        kdom_util_cython.k_dom_by_points_cython(p, kValue, pointBuffer)
    end_time = time.time()
    secs = end_time - start_time
    print(secs)

if __name__ == '__main__':
    pathName = os.path.dirname(os.path.abspath(__file__))
    buf = np.loadtxt(pathName + "\data\data_corr_100_11_0.db", delimiter=",")
    calc_pure_python_performance(buf, buf[0], 11)
    calc_pure_python_performance2(buf, buf[0], 11)
    #calc_cpython_kdombypoints_performance(buf, 11)
    calc_pure_python_kdombypoints_performance(buf, 11)
