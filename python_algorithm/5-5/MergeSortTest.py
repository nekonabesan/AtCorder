import unittest
from MergeSort import MergeSort

class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.sorter = MergeSort()

    def test(self):
        self.assertEqual(self.sorter.sort([], []), [])
        self.assertEqual(self.sorter.sort([42], []), [42])
        self.assertEqual(self.sorter.sort([1, 3, 4, 7, 8, 9], [0, 2, 5, 6]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()