import unittest
from Stack import Stack

class StackTets(unittest.TestCase):

    def test(self):
        S = Stack()
        ######################################################
        # push
        ######################################################
        S.push(0)
        a1 = S.sp
        self.assertEqual(S.sp.value, 0)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, None)
        S.push(1)
        a2 = S.sp
        self.assertEqual(S.sp.value, 1)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a1)
        self.assertEqual(a1.prev, a2)
        S.push(2)
        a3 = S.sp
        self.assertEqual(S.sp.value, 2)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a2)
        self.assertEqual(a2.prev, a3)
        S.push(3)
        a4 = S.sp
        self.assertEqual(S.sp.value, 3)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a3)
        self.assertEqual(a3.prev, a4)
        S.push(4)
        a5 = S.sp
        self.assertEqual(S.sp.value, 4)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a4)
        self.assertEqual(a4.prev, a5)
        ######################################################
        # pop
        ######################################################
        value = S.pop()
        print("pop1", value)
        pop1 = S.sp
        self.assertEqual(value, 4)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a3)
        self.assertEqual(a3.prev, pop1)
        value = S.pop()
        print("pop2", value)
        pop2 = S.sp
        self.assertEqual(value, 3)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a2)
        self.assertEqual(a2.prev, pop2)
        value = S.pop()
        print("pop3", value)
        pop3 = S.sp
        self.assertEqual(value, 2)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, a1)
        self.assertEqual(a1.prev, pop3)
        value = S.pop()
        print("pop4", value)
        pop4 = S.sp
        self.assertEqual(value, 1)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, None)
        self.assertEqual(pop4.next, None)
        value = S.pop()
        print("pop5", value)
        pop5 = S.sp
        self.assertEqual(value, 0)
        self.assertEqual(S.sp.value, None)
        self.assertEqual(S.sp.prev, None)
        self.assertEqual(S.sp.next, None)
        self.assertEqual(pop5.value, None)
    

if __name__ == '__main__':
    unittest.main()