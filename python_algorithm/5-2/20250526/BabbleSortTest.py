import unittest
from BabbleSort import BabbleSort

class TestBabbleSort(unittest.TestCase):
    def test(self):
        B = BabbleSort()
        self.assertEqual(B.sort(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()