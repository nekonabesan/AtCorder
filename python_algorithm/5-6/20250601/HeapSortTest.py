import unittest
from HeapSort import HeapSort

class HeapSortTest(unittest.TestCase):
    def test(self):
        H = HeapSort()
        data = [60, 49, 84, 58, 95, 15, 31, 11, 96, 40, 11]
        self.assertEqual(H.sort(data), [11, 11, 15, 31, 40, 49, 58, 60, 84, 95, 96])

        

if __name__ == '__main__':
    unittest.main()