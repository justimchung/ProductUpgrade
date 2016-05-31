from DynamicBuffer import *
import unittest

class TestUtil(unittest.TestCase):
    def setUp(self):
        self.dBUffer = DynamicBuffer(10, 2)

    def test_appendData(self):
        self.dBUffer.append([10, 10])
        self.assertEqual(len(self.dBUffer), 1)

    def test_buffer_resize(self):
        for i in range(15):
            self.dBUffer.append([10, 10])

        self.assertEqual(len(self.dBUffer), 15)

    def testLen(self):
        self.assertEqual(len(self.dBUffer), 0)

    def test_sortByDim(self):
        self.dBUffer.append([1,2])
        self.dBUffer.append([4,1])
        self.dBUffer.append([0,0])
        self.dBUffer.sortByDim(1)
        self.assertEqual(self.dBUffer.buffer[0][0], 0)
        self.assertEqual(self.dBUffer.buffer[2][0], 1)

if __name__ == '__main__':
    unittest.main()

