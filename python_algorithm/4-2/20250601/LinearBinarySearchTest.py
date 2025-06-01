import unittest
from LinearBinarySearch import LinearBinarySearch

class LinearBinarySearchTest(unittest.TestCase):
    def test(self):
        l = LinearBinarySearch()
        data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93, 100]
        # 線形リスト初期化
        node = l.init_data(data)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 100)
        self.assertEqual(l.length, 15)
        self.assertEqual(l.tp, node)
        # headとtailの確認
        head = l.head()
        self.assertEqual(head.value, 1)
        self.assertIsNone(head.prev)
        self.assertIsNotNone(head.next)
        tail = l.tail()
        self.assertEqual(tail.index, 14)
        self.assertEqual(tail.value, 100)
        self.assertIsNone(tail.next)
        # 線形リストのインデックスを取得
        node = l.get_node_by_index(-1)
        self.assertIsNone(node)
        node = l.get_node_by_index(0)
        self.assertIsNotNone(node)
        node = l.get_node_by_index(14)
        self.assertIsNotNone(node)
        node = l.get_node_by_index(15)
        self.assertIsNone(node)
        # 二分探索
        node = l.search(0, l.length - 1, 1)
        self.assertIsNotNone(node.value, 1)
        node = l.search(0, l.length - 1, 78)
        self.assertIsNotNone(node.value, 78)
        node = l.search(0, l.length - 1, 100)
        self.assertIsNotNone(node.value, 100)

        # Test search        
        # Test head and tail
        #self.assertEqual(l.head().value, 1)
        #self.assertEqual(l.tail().value, 5)
        
        

if __name__ == '__main__':
    unittest.main()
