from util import *
class DynamicBuffer():
    def __init__(self, datatype, size, dim):
        self.dimension = dim
        self.size = size
        self.length = 0
        self._buffer = np.empty((size, dim))

    def __len__(self):
        return self.length

    def append(self, point):
        if self.length == self.size:
            self.size = int(1.5 * self.size)
            self._buffer.resize((self.size, self.dimension), refcheck=False)
            self._buffer[self.length] = point
            self.length += 1

    @property
    def buffer(self):
        return self._buffer[:self.length]