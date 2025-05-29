import unittest
from BinarySearch import BinarySearch

class BinarySearchTest(unittest.TestCase):
    def test(self):
        B = BinarySearch()
        self.assertEqual(B.search(72), True)
        

if __name__ == '__main__':
    unittest.main()