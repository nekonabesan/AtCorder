import unittest
from InsertSort import InsertSort

class InsertSortTest(unittest.TestCase):
    def test(self):
        I = InsertSort()
        self.assertEqual(I.sort([9, 2, 4, 7, 8, 3, 1, 5, 6, 0]), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == '__main__':
    unittest.main()