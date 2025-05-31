import unittest
from ShellSort import ShellSort
class ShellSortTest(unittest.TestCase):
    def test_empty_list(self):
        S = ShellSort()
        cnt, A = S.sort([5, 1, 4, 3, 2], 5)
        self.assertEqual(A, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()