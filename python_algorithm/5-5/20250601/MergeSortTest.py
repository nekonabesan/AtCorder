import unittest
from MergeSort import MergeSort

class MergeSortTest(unittest.TestCase):
    def test(self):
        data = [12, 13, 47, 78, 20, 72, 97, 56, 22, 32, 57, 20, 44, 52, 84]
        M = MergeSort(data)
        self.assertEqual(M.sort(0, 7, 15), [12, 13, 20, 20, 22, 32, 44, 47, 52, 56, 57, 72, 78, 84, 97])



if __name__ == '__main__':
    unittest.main()