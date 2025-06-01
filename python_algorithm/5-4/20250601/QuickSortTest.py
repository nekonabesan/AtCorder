import unittest
from QuickSort import QuickSort

class QuickSortTest(unittest.TestCase):
    def test(self):
        data  = [2, 52, 40, 57, 97, 90, 64, 26, 93, 9, 58, 38, 25, 47, 92]
        Q = QuickSort(data)
        Q.sort(0, len(data) - 1)
        self.assertEqual(Q.data, [2, 9, 25, 26, 38, 40, 47, 52, 57, 58, 64, 90, 92, 93, 97])

if __name__ == '__main__':
    unittest.main()