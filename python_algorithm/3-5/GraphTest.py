import unittest
from Graph import Graph

class GraphTest(unittest.TestCase):
    def test(self):
        G = Graph()
        ret = G.walk()
        expected = [
            "(0) --> (1)",
            "(0) --> (2)",
            "(1) --> (2)",
            "(1) --> (3)",
            "(2) <-- (4)",
            "(3) <--> (4)"
        ]
        self.assertEqual(ret[0], expected[0])
        self.assertEqual(ret[1], expected[1])
        self.assertEqual(ret[2], expected[2])
        self.assertEqual(ret[3], expected[3])
        self.assertEqual(ret[4], expected[4])
        self.assertEqual(ret[5], expected[5])

        

if __name__ == '__main__':
    unittest.main()