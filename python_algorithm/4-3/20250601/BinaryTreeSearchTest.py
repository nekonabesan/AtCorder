import unittest
from BinaryTreeSearch import BinaryTreeSearch

class BinaryTreeSearchTest(unittest.TestCase):
    def test(self):
        tree = BinaryTreeSearch()
        # 2分木構造を構築
        root = tree.insert(10, None)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root, root)

        node5 = tree.insert(5, root, pl=True)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.left, node5)

        node2 = tree.insert(2, node5, pl=True)
        self.assertEqual(tree.root.left.left.value, 2)
        self.assertEqual(tree.root.left.left, node2)

        node8 = tree.insert(8, node5, pr=True)
        self.assertEqual(tree.root.left.right.value, 8)
        self.assertEqual(tree.root.left.right, node8)

        node6 = tree.insert(6, node8, pl=True)
        self.assertEqual(tree.root.left.right.left.value, 6)
        self.assertEqual(tree.root.left.right.left, node6)

        node9 = tree.insert(9, node8, pr=True)
        self.assertEqual(tree.root.left.right.right.value, 9)
        self.assertEqual(tree.root.left.right.right, node9)

        node12 = tree.insert(12, root, pr=True)
        self.assertEqual(tree.root.right.value, 12)
        self.assertEqual(tree.root.right, node12)

        node11 = tree.insert(11, node12, pl=True)
        self.assertEqual(tree.root.right.left.value, 11)
        self.assertEqual(tree.root.right.left, node11)
        # データ取得
        tree.tarverse(tree.root)
        self.assertEqual(tree.ret, [2, 5, 6, 8, 9, 10, 11, 12])
        
        pass

if __name__ == '__main__':
    unittest.main()

