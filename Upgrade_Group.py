from util import *
from DynamicBuffer import DynamicBuffer
class UpgradeGroup:
    """
    UpgradeGroup is a buffer that stores a set of skyline points which
     dominate a product in the same subspace.
     self.product is the product that is dominated by all the skyline points in the same subspace.
     self.subspace is the subspace on which the product are worse than the skyline points
     self.dBuffer is a buffer that store all the skyline points
    """
    def __init__(self, product, subspace, size, dim, datatype='uint32') :
        self.product = product
        self.subspace = subspace
        self.Dim = dim
        self.dBuffer = DynamicBuffer(size, dim, datatype)

    def addSkylinePoint(self, prod):
        self.dBuffer.append(prod)

    def getSkylineBuffer(self):
        """
        return the buffer that stores the skyline points
        :return: the buffer that stores the skyline points
        """
        return self.dBuffer.buffer

    def getSubspace(self):
        return self.subspace

    def getProduct(self):
        return self.product


    def sortByDim(self, dim):
        self.dBuffer.sortByDim(dim)

    def getDIM(self):
        return self.Dim
