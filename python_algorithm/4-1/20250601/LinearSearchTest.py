import unittest
from LinearSearch import LinearSearch

class LinearSearchTest(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
        self.search = LinearSearch(self.data)

    def test_init_data(self):
        self.search.init_data()
        self.assertEqual(self.search.hd.value, 1)
        self.assertEqual(self.search.td.value, 5)

    def test_head(self):
        self.search.init_data()
        head = self.search.head()
        self.assertEqual(head.value, 1)

    def test_tail(self):
        self.search.init_data()
        tail = self.search.tail()
        self.assertEqual(tail.value, 5)

    def test_search_found(self):
        self.search.init_data()
        result = self.search.search(3)
        self.assertIsNotNone(result)
        self.assertEqual(result.value, 3)

    def test_search_not_found(self):
        self.search.init_data()
        result = self.search.search(6)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()