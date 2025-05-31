import unittest
from BubbleSort import BubbleSort

class BubbleSortTest(unittest.TestCase):
    def test(self):
        sorter = BubbleSort()
        A = [5, 3, 2, 4, 1]
        c, A = sorter.sort(A, len(A))
        self.assertEqual(c, 8)
        self.assertEqual(A, [1, 2, 3, 4, 5])
        A = [1, 2, 3, 4, 5]
        c, A = sorter.sort(A, len(A))
        self.assertEqual(c, 0)
        self.assertEqual(A, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()