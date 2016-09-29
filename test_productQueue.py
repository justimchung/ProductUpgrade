import unittest
from product_queue import productQueue
from upgrade_product import upgProduct
import numpy as np

class TestProductQueue(unittest.TestCase):
    def setUp(self):
        self.queue = productQueue()
        self.p1 = upgProduct(np.array([3,4,5], dtype='int32'))
        self.p1.setCost(30)
        self.p2 = upgProduct(np.array([4,5,6], dtype='int32'))
        self.p2.setCost(40)
        self.p3 = upgProduct(np.array([7,8,7], dtype='int32'))
        self.p3.setCost(35)
    def test_push(self):
        self.queue.push(self.p1)
        self.queue.push(self.p2)
        self.queue.push(self.p3)
        self.assertEqual(3, self.queue.getSize())

    def test_pop(self):
        self.queue.push(self.p1)
        self.queue.push(self.p2)
        self.queue.push(self.p3)
        p = self.queue.pop()
        self.assertEqual(30, p.getCost())
        self.assertTrue(np.array_equal(p.attributes, np.array([3,4,5], dtype='int32')))
        p = self.queue.pop()
        self.assertEqual(35, p.getCost())
        self.assertTrue(np.array_equal(p.attributes, np.array([7,8,7], dtype='int32')))
        p = self.queue.pop()
        self.assertEqual(40, p.getCost())
        self.assertTrue(np.array_equal(p.attributes, np.array([4,5,6], dtype='int32')))

    def test_getSize(self):
        self.assertEqual(0, self.queue.getSize())
        self.queue.push(self.p1)
        self.queue.push(self.p2)
        self.assertEqual(2, self.queue.getSize())

if __name__ == '__main__':
    unittest.main()
