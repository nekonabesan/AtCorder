import unittest
from TreeSearch import TreeSearch

class TestTreeSearch(unittest.TestCase):
    def test(self):
        T = TreeSearch()
        T.traverse(0)


if __name__ == '__main__':
    unittest.main()