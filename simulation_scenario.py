import util
import numpy as np
import simulator as sim

numIteration = 10 #number of iterations for each test
defaultDim = 11
defaultDataSize = 100
datasizeIndex = 0
dimIndex = 1
kValueIndex = 2
distIndex = 3
algIndex = 4


def getDataFileName(dist, dim, iter):
    fname = 'data_%s_%d_%d_%d.db' % (dist, dim, iter)
    return fname


def effect_k_scenario():
    kvalues = [6, 7, 8, 9, 10]
    dims = np.full(1, defaultDim, dtype='int32')
    datasizes = np.full(1, defaultDataSize, dtype='int32')
    dists = np.array(['corr', 'uni', 'anti'])
    algNames = np.array(['Upgrade_Algorithm', 'New_Upgrade_Algorithm'])
    simSettings = util.cartesian(datasizes, dims, kvalues, dists, algNames)
    for setting in simSettings:
        for iter in range(numIteration):
            fileName = getDataFileName(setting[distIndex], setting[dimIndex], iter)
            sim.simulator(kValue=setting[kValueIndex], fileName=fileName, algName=setting[algIndex], product=np.array([10,10,10]))

