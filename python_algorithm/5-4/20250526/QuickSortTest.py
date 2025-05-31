import unittest
from QuickSort import QuickSort

class QuickSortTest(unittest.TestCase):
    def test(self):
        Q = QuickSort()
        self.assertEqual(Q.sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(Q.sort([]), [])
        self.assertEqual(Q.sort([5]), [5])
        self.assertEqual(Q.sort([2, 1]), [1, 2])
        self.assertEqual(Q.sort([1, 2]), [1, 2])

if __name__ == '__main__':
    unittest.main()