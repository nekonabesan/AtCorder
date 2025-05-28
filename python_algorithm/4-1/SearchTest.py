import unittest
from Search import Search

class TestSearch(unittest.TestCase):
    def test(self):
        search = Search()
        # Test with an element that exists in the list
        self.assertTrue(search.execute(57), "Should return True for existing element 57")
        # Test with an element that does not exist in the list
        self.assertFalse(search.execute(100), "Should return False for non-existing element 100")
        # Test with another existing element
        self.assertTrue(search.execute(49), "Should return True for existing element 49")
        # Test with an element that is not in the list
        self.assertFalse(search.execute(30), "Should return False for non-existing element 30")
        

if __name__ == '__main__':
    unittest.main()