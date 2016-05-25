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

if __name__ == '__main__':
    unittest.main()

