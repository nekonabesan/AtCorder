import unittest
from Linkedlist import LinkedList

class LinkedListTest(unittest.TestCase):
    def test(self):
        L = LinkedList()
        L.add_list(0)
        self.assertEqual(L.data, [0, None, None, None, None])
        self.assertEqual(L.pointer, [None, None, None, None, None])
        self.assertEqual(L.head, 0)
        L.add_list(1)
        self.assertEqual(L.data, [0, 1, None, None, None])
        self.assertEqual(L.pointer, [1, None, None, None, None])
        self.assertEqual(L.head, 0)
        L.add_list(2)
        self.assertEqual(L.data, [0, 1, 2, None, None])
        self.assertEqual(L.pointer, [1, 2, None, None, None])
        self.assertEqual(L.head, 0)
        L.add_list(3)
        self.assertEqual(L.data, [0, 1, 2, 3, None])
        self.assertEqual(L.pointer, [1, 2, 3, None, None])
        self.assertEqual(L.head, 0)
        L.add_list(4)
        self.assertEqual(L.data, [0, 1, 2, 3, 4])
        self.assertEqual(L.pointer, [1, 2, 3, 4, None])
        self.assertEqual(L.head, 0)
        L.add_list(5)
        self.assertEqual(L.data, [0, 1, 2, 3, 4])
        self.assertEqual(L.pointer, [1, 2, 3, 4, None])
        self.assertEqual(L.head, 0)
        L.del_list(3)
        self.assertEqual(L.data, [0, 1, 2, None, 4])
        self.assertEqual(L.pointer, [1, 2, 4, None, None])
        self.assertEqual(L.head, 0)
        L.del_list(0)
        self.assertEqual(L.data, [None, 1, 2, None, 4])
        self.assertEqual(L.pointer, [None, 2, 4, None, None])
        self.assertEqual(L.head, 1)
        L.add_list(5)
        self.assertEqual(L.data, [5, 1, 2, None, 4])
        self.assertEqual(L.pointer, [None, 2, 4, None, 0])
        self.assertEqual(L.head, 1)
        L.del_list(0)
        self.assertEqual(L.data, [5, 1, 2, None, 4])
        self.assertEqual(L.pointer, [None, 2, 4, None, 0])
        self.assertEqual(L.head, 1)
        L.del_list(4)
        self.assertEqual(L.data, [5, 1, 2, None, None])
        self.assertEqual(L.pointer, [None, 2, 0, None, None])
        self.assertEqual(L.head, 1)
        L.del_list(5)
        self.assertEqual(L.data, [None, 1, 2, None, None])
        self.assertEqual(L.pointer, [None, 2, None, None, None])
        self.assertEqual(L.head, 1)
        L.del_list(1)
        self.assertEqual(L.data, [None, None, 2, None, None])
        self.assertEqual(L.pointer, [None, None, None, None, None])
        self.assertEqual(L.head, 2)
        L.del_list(2)
        self.assertEqual(L.data, [None, None, None, None, None])
        self.assertEqual(L.pointer, [None, None, None, None, None])
        self.assertEqual(L.head, 0)
        

if __name__ == '__main__':
    unittest.main()