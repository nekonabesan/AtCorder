import unittest
from InsertSort import InsertSort

class InsertSortTest(unittest.TestCase):
    sort = InsertSort()
    def test(self):
        #self.assertEqual(self.sort.sort([5, 2, 9, 1, 5, 6], 6), [1, 2, 5, 5, 6, 9])
        self.assertEqual(self.sort.sort([5, 2, 4, 6, 1, 3], 6), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()