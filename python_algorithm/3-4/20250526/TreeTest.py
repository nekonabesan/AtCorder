import unittest
from Tree import Tree

class TreeTest(unittest.TestCase):
    def test(self):
        tree = Tree()
        # Test the root node
        ret, left, right = tree.walk(0)
        print(ret)
        self.assertEqual(ret, 10)
        self.assertEqual(left, 1)
        self.assertEqual(right, 2)
        
        # Test left child of root
        ret, left, right = tree.walk(1)
        self.assertEqual(ret, 20)
        self.assertEqual(left, 3)
        self.assertEqual(right, 4)
        
        # Test right child of root
        ret, left, right = tree.walk(2)
        self.assertEqual(ret, 30)
        self.assertEqual(left, 5)
        self.assertEqual(right, None)
        
        # Test left child of left child
        ret, left, right = tree.walk(3)
        self.assertEqual(ret, 40)
        self.assertEqual(left, None)
        self.assertEqual(right, None)
        
        # Test right child of left child
        ret, left, right = tree.walk(4)
        self.assertEqual(ret, 50)
        self.assertEqual(left, 6)
        self.assertEqual(right, 7)
        
        # Test left child of right child
        ret, left, right = tree.walk(5)
        self.assertEqual(ret, 60)
        self.assertEqual(left, None)
        self.assertEqual(right, None)
        
        # Test right child of right child
        ret, left, right = tree.walk(6)
        self.assertEqual(ret, 70)
        self.assertEqual(left, None)
        self.assertEqual(right, None)

        # Test right child of right child
        ret, left, right = tree.walk(7)
        self.assertEqual(ret, 80)
        self.assertEqual(left, None)
        self.assertEqual(right, None)

if __name__ == '__main__':
    unittest.main()