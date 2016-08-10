import util
import numpy as np
import simulator as sim
import logging
import logging.handlers
import os

numIteration = 5 #number of iterations for each test
defaultDim = 11
defaultDataSize = 100
datasizeIndex = 1
dimIndex = 2
kValueIndex = 4
distIndex = 3
algIndex = 0
SimulationLogFileName = 'Product_Upgrade_Sim_log.log'
LoggerName = 'upgrade_product_logger'

def getCurrentPath():
    return os.path.dirname(os.path.abspath(__file__))

def getDataFileName(dist, datasize, dim, iter):
    fname = getCurrentPath() + '\data\data_%s_%d_%d_%d.db' % (dist, datasize, dim, iter)
    return fname

def getProductFileName(dim):
    fname = getCurrentPath() + '\data\product_uni_1_%d_0.db' % (dim)
    return fname

def effect_k_scenario():
    logger = logging.getLogger('upgrade_product_logger')
    logger.debug('Effect of K simulation')
    kvalues = [6, 7, 8, 9, 10]
    dims = np.full(1, defaultDim, dtype='int32')
    datasizes = np.full(1, defaultDataSize, dtype='int32')
    dists = np.array(['corr', 'uni', 'anti'])
    algNames = np.array(['Upgrade_Algorithm', 'New_Upgrade_Algorithm'])
    simSettings = generate_simulation_settings(algNames, datasizes, dims, dists, kvalues)
    for setting in simSettings:
        ProductFileName = getProductFileName(int(setting[dimIndex]))
        ProductBuffer = np.loadtxt(ProductFileName, delimiter=',', dtype='int32')
        ProductIndex = 0
        for iter in range(numIteration):
            DataFileName = getDataFileName(setting[distIndex], int(setting[datasizeIndex]), int(setting[dimIndex]), iter)
            logger.debug('[info]Dist = %s, dataSize = %d, dim = %d, k = %d, iter = %d data_file = %s' %
                         (setting[distIndex], int(setting[datasizeIndex]), int(setting[dimIndex]),
                          int(setting[kValueIndex]), iter, DataFileName))
            aSim = sim.simulator(kValue=int(setting[kValueIndex]), fileName=DataFileName, algName=setting[algIndex],
                          product=ProductBuffer[ProductIndex])
            aSim.run()
            ProductIndex += 1


def generate_simulation_settings(algNames, datasizes, dims, dists, kvalues):
    simSettings = util.cartesian((algNames, datasizes, dims, dists, kvalues))
    return simSettings


def initial_logging():
    logger = logging.getLogger(LoggerName)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(SimulationLogFileName)
    logger.addHandler(handler)


if __name__ == '__main__':
    initial_logging()
    effect_k_scenario()
