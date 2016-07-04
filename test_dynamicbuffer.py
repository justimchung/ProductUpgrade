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

    def test_constructorWithSkylineBuffer(self):
        sBuf = np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])
        aDynamicBuffer = DynamicBuffer(1, 0, skyBuf = sBuf)
        self.assertEqual(len(aDynamicBuffer), 4)
        self.assertTrue(np.array_equal(aDynamicBuffer.buffer, np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])))

    def test_appendBuffer(self):
        sBuf = np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])
        aDynamicBuffer = DynamicBuffer(2, 3)
        aDynamicBuffer.appendBuffer(sBuf)
        self.assertEqual(len(aDynamicBuffer), 4)
        self.assertTrue(np.array_equal(aDynamicBuffer.buffer, np.array([[1,2,3], [4,5,6], [7,8,9],[10,11,12]])))

if __name__ == '__main__':
    unittest.main()

