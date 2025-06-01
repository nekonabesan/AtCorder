import unittest
from BabbleSort import BabbleSort

class BabbleSortTest(unittest.TestCase):
    def test(self):
        b = BabbleSort()
        self.assertEqual(b.sort([9, 4, 7, 2, 3, 8, 6, 1, 5, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()