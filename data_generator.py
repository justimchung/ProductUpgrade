#!/usr/bin/env python
from numpy.random import *
from math import pow
from pylab import *
import string

valueLowerBound = 0
valueUpperBound = 100
# The dimensionality of data
cDim = 4
# variance for corr data set
cVar = 15
# variance for corr data set
cVar2 = 5
# variance for anti_corr data set
cVar_Anti = 3


def selectAPoint(aVar):
    return normal((valueUpperBound - valueLowerBound) / 2.0, aVar)


def selectAPointNearT_Normal(T, aVar, aDim):
    point = []
    for i in range(aDim):
        point.append(normal(T, aVar))
    return point


def selectAPointNearT_Uniform(T, aDim):
    point = []
    for i in range(aDim):
        v = 0.0
        while True:
            v = uniform(valueLowerBound, valueUpperBound)
            if (v >= valueLowerBound and v <= valueUpperBound):
                break
        point.append(v)
    return point


def calculateK(point, T):
    k = 0.0
    aDIM = len(point)
    for i in range(aDIM):
        k = k + point[i] * (1 - T)
    k = k - aDIM * (T * (1 - T))
    return k


def calculateBase(T, aDIM):
    return aDIM * pow(1 - T, 2)


def calculateProjectPointToAPlan(point, T, aDIM):
    project = []
    k = calculateK(point, T)
    base = calculateBase(T, aDIM)
    param = 1 - T
    for i in range(aDIM):
        project.append(point[i] - (param * k / base))
    return project


def generate_Anti_Points(numPoints, aDIM):
    points = []
    for i in range(numPoints):
        T = selectAPoint(cVar)
        pnt = selectAPointNearT_Normal(T, cVar2, aDIM)
        points.append(calculateProjectPointToAPlan(pnt, T, aDIM))
    return points


def generate_Corr_Points(numPoints, aDIM):
    points = []
    for i in range(numPoints):
        T = selectAPoint(cVar_Anti)
        pnt = selectAPointNearT_Uniform(T, aDIM)
        points.append(calculateProjectPointToAPlan(pnt, T, aDIM))
    return points


def generate_Uni_Points(numPoints, aDIM):
    points = []
    for i in range(numPoints):
        pt = []
        for j in range(aDIM):
            pt.append(uniform(valueLowerBound, valueUpperBound))
        points.append(pt)
    return points


# can only draw 2D graphic
def plot_Data_Points(points):
    xList = []
    yList = []
    for i in range(len(points)):
        xList.append(points[i][0])
        yList.append(points[i][1])

    plot(xList, yList, 'o', ms=1)


def set_Lower_Bound(aBound):
    global valueLowerBound
    valueLowerBound = aBound


def set_Upper_Bound(aBound):
    global valueUpperBound
    valueUpperBound = aBound


def saveDataItemsToFile(fname, points):
    f = open(fname, "w")
    for i in range(len(points)):
        s = "%d,%s\n" % ((i + 1), (','.join(["%.3f" % (k) for k in points[i]])))
        f.write(s)
    f.close()


def GenerateDataForNum_DataItems():
    # Generate data for number of data items
    dataItems = [100000, 250000, 500000, 750000, 1000000]
    # dataItems = [5000]
    d = 8
    for di in dataItems:
        for iter in range(5):
            points = generate_Anti_Points(di, d)
            saveDataItemsToFile("data_anti_%d_%d_%d.db" % (di / 1000, d, iter), points)

            points = generate_Corr_Points(di, d)
            saveDataItemsToFile("data_corr_%d_%d_%d.db" % (di / 1000, d, iter), points)

            points = generate_Uni_Points(di, d)
            saveDataItemsToFile("data_uni_%d_%d_%d.db" % (di / 1000, d, iter), points)


def GenerateDataForNum_Dimensionalities():
    di = 500000
    for d in range(4, 18, 2):
        if d == 8:
            continue
        for iter in range(5):
            points = generate_Uni_Points(di, d)
            saveDataItemsToFile("data_uni_%d_%d_%d.db" % (di / 1000, d, iter), points)
            points = generate_Corr_Points(di, d)
            saveDataItemsToFile("data_corr_%d_%d_%d.db" % (di / 1000, d, iter), points)
            points = generate_Anti_Points(di, d)
            saveDataItemsToFile("data_anti_%d_%d_%d.db" % (di / 1000, d, iter), points)


if __name__ == "__main__":
    for iter in range(5):
        points = generate_Uni_Points(20000, 7)
        saveDataItemsToFile("data_uni_%d_%d_%d.db" % (20, 7, iter), points)
        # GenerateDataForNum_DataItems()
        # GenerateDataForNum_DataItems()
        # GenerateDataForNum_Dimensionalities()
        # for i in range(100):
        #    print "%d %s" % (i, ','.join(["%.3f" % (k) for k in points[i]]))


        # for i in range(1000):
        #    print "%s" % (','.join(["%.3f" % (k) for k in points[i]]))
        # points = generate_Uni_Points(500, 2)
        # plot_Data_Points(points)

        # set the tick of the axis
        # axis([valueLowerBound, valueUpperBound, valueLowerBound, valueUpperBound], 'equal')

        # savefig('./Uni.eps')






