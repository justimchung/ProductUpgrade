from DynamicBuffer import *
import unittest

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.dBuffer = DynamicBuffer(10, 2)

    def test_appendData(self):
        self.dBuffer.append([10, 10])
        self.assertEqual(len(self.dBuffer), 1)

    def test_buffer_resize(self):
        for i in range(15):
            self.dBuffer.append([10, 10])

        self.assertEqual(len(self.dBuffer), 15)

    def testLen(self):
        self.assertEqual(len(self.dBuffer), 0)

    def test_sortByDim(self):
        self.dBuffer.append([1, 2])
        self.dBuffer.append([4, 1])
        self.dBuffer.append([0, 0])
        self.dBuffer.sortByDim(1)
        self.assertEqual(self.dBuffer.buffer[0][0], 0)
        self.assertEqual(self.dBuffer.buffer[2][0], 1)

if __name__ == '__main__':
    unittest.main()

