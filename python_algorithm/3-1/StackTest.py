import unittest
from Stack import Stack

class StackTets(unittest.TestCase):

    def test(self):
        S = Stack()
        S.push(0)
        self.assertEqual(S.stack, [0, None, None, None, None])
        self.assertEqual(S.sp, 1)
        S.push(1)
        self.assertEqual(S.stack, [0, 1, None, None, None])
        self.assertEqual(S.sp, 2)
        S.push(2)
        self.assertEqual(S.stack, [0, 1, 2, None, None])
        self.assertEqual(S.sp, 3)
        S.push(3)
        self.assertEqual(S.stack, [0, 1, 2, 3, None])
        self.assertEqual(S.sp, 4)
        S.push(4)
        self.assertEqual(S.stack, [0, 1, 2, 3, 4])
        self.assertEqual(S.sp, 5)
        v = S.pop()
        self.assertEqual(S.stack, [0, 1, 2, 3, None])
        self.assertEqual(v, 4)
        v = S.pop()
        self.assertEqual(S.stack, [0, 1, 2, None, None])
        self.assertEqual(v, 3)
        v = S.pop()
        self.assertEqual(S.stack, [0, 1, None, None, None])
        self.assertEqual(v, 2)
        v = S.pop()
        self.assertEqual(S.stack, [0, None, None, None, None])
        self.assertEqual(v, 1)
        v = S.pop()
        self.assertEqual(S.stack, [None, None, None, None, None])
        self.assertEqual(v, 0)
        v = S.pop()
        S.push(99)
        self.assertEqual(S.stack, [99, None, None, None, None])
        self.assertEqual(S.sp, 1)
        v = S.pop()
        self.assertEqual(S.stack, [None, None, None, None, None])
        self.assertEqual(v, 99)
        print(S.stack)

    

if __name__ == '__main__':
    unittest.main()