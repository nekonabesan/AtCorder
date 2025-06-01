import unittest
from Dijkstra import Dijkstra

class DijkstraTest(unittest.TestCase):
    def test(self):
        D = Dijkstra()
        D.dijkstra()
        dist,route = D.get_distances(0, 6)
        
        pass

if __name__ == '__main__':
    unittest.main()