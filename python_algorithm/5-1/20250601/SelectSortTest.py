import unittest
from SelectSort import SelectSort

class SelectSortTest(unittest.TestCase):
    def test_select_sort(self):
        s = SelectSort()
        self.assertEqual(s.sort([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])
        self.assertEqual(s.sort([3, 0, -2, 8, -1]), [-2, -1, 0, 3, 8])
        self.assertEqual(s.sort([]), [])
        self.assertEqual(s.sort([1]), [1])
        self.assertEqual(s.sort([2, 2, 2]), [2, 2, 2])
        self.assertEqual(s.sort([9, 3, 7, 1, 4, 2, 5, 8, 6, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()