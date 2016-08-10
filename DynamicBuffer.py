# -*- coding:utf-8 -*-
from util import *
class DynamicBuffer():
    def __init__(self, size, dim, datatype='uint32', **kwargs):
        """
        初始化 DynamicBuffer
        :param size: the initial size of the buffer
        :param dim: the dimensionality of the data item in the buffer
        :param datatype: the data type of each element in a data item
        :param kwargs: the optional parameter. Currently, the only optional parameter is 'skyBuf'.
          skyBuf stands for the 'buffer of a set of skyline points'
        """
        if 'skyBuf' not in kwargs:
            self.dimension = dim
            self.size = size
            self.length = 0
            self._buffer = np.empty((size, dim), dtype=datatype)
            self._buffer = np.full((size, dim), np.inf)
        else:
            self._buffer = kwargs['skyBuf']
            self.size = self._buffer.shape[0]
            self.length = self.size
            self.dimension = self._buffer.shape[1]

    def __len__(self):
        return self.length

    def append(self, point):
        if self.length == self.size:
            self.size = int(1.5 * self.size)
            self._buffer.resize((self.size, self.dimension), refcheck=False)
        self._buffer[self.length:,].fill(np.inf)
        self._buffer[self.length] = point
        self.length += 1

    def appendBuffer(self, points):
        """
        append a set of data points into the buffer
        """
        for p in points:
            self.append(np.array(p, dtype='int32'))

    def sortByDim(self, dim):
        """
        Sort the buffer in ascending order of the dim-th dimension.
        :param dim: the dime
        """
        self._buffer = self._buffer[self._buffer[:,dim].argsort()]


    @property
    def buffer(self):
        return self._buffer[:self.length]