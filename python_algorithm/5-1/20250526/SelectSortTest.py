import unittest
from SelectSort import SelectSort

class TestSelectSort(unittest.TestCase):
    def test(self):
        S = SelectSort()
        self.assertEqual(S.sort(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    unittest.main()