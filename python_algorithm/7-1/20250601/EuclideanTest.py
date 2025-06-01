import unittest
from Euclidean import Euclidean

class EuclideanTest(unittest.TestCase):
    def test(self):
        euclidean = Euclidean()
        self.assertEqual(euclidean.euclid(48, 18), 6)
        self.assertEqual(euclidean.euclid(56, 98), 14)
        self.assertEqual(euclidean.euclid(101, 10), 1)
        

if __name__ == '__main__':
    unittest.main()