import unittest
from Tree import Tree

class TreeTest(unittest.TestCase):
    def test(self):
        tree = Tree()
        root = tree.root
        self.assertIsNone(root.value)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)
        root.value = 10
        tree.add_child(root, 20, 30)
        self.assertEqual(root.value, 10)
        self.assertEqual(root.left.value, 20)
        self.assertEqual(root.right.value, 30)
        c20 = tree.find(20, root)
        parent = tree.add_child(c20, 40, 50)
        self.assertEqual(c20.value, 20)
        self.assertEqual(c20.left.value, 40)
        self.assertEqual(c20.right.value, 50)
        c50 = tree.find(50, parent)
        tree.add_child(c50, 70, 80)

        pass

if __name__ == '__main__':
    unittest.main()