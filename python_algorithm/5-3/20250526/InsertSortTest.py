import unittest
from InsertSort import InsertSort

class TestInsertSort(unittest.TestCase):
    def test(self):
        I = InsertSort()
        self.assertEqual(I.sort(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()