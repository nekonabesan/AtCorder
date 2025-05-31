import unittest
from MergeSort import MergeSort

class MergeSortTest(unittest.TestCase):
    def test(self):
        M = MergeSort()
        cnt,A = M.merge_sort([8, 5, 9, 2, 6, 3, 7, 1, 10, 4], 10, 0, 10)
        self.assertEqual(cnt, 34)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == '__main__':
    unittest.main()