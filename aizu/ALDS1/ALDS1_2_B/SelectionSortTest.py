import unittest
from SelectionSort import SelectionSort

class SelectonSortTest(unittest.TestCase):
    def test_selection_sort(self):
        S = SelectionSort()
        c, A = S.sort([5, 6, 4, 2, 1, 3], 6)
        self.assertEqual(c, 4)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
        c, A = S.sort([100], 1)
        self.assertEqual(c, 0)
        self.assertEqual(A, [100])


if __name__ == '__main__':
    unittest.main()