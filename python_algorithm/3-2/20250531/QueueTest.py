import unittest
from Queue import Queue

class QueueTest(unittest.TestCase):
    def test(self):
        queue = Queue()
        ret = queue.dequeue()
        ret = queue.enqueue(0)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.head(), ret)
        self.assertEqual(queue.head(), queue.tail())
        self.assertEqual(queue.tail(), ret)
        ret = queue.enqueue(1)
        self.assertEqual(queue.size(), 2)
        self.assertEqual(queue.head().value, 0)
        self.assertEqual(queue.tail().value, 1)
        self.assertEqual(queue.head().next, queue.tail())
        self.assertEqual(queue.tail().prev, queue.head())
        self.assertEqual(queue.head().next.value, 1)
        self.assertEqual(queue.tail().prev.value, 0)
        ret = queue.enqueue(2)
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.head().value, 0)
        self.assertEqual(queue.tail().value, 2)
        self.assertEqual(queue.head().next.value, 1)
        self.assertEqual(queue.tail().prev.value, 1)
        self.assertEqual(queue.head().next.next.value, 2)
        self.assertEqual(queue.tail().prev.prev.value, 0)
        self.assertEqual(queue.head().next.next, queue.tail())
        self.assertEqual(queue.tail().prev.prev, queue.head())
        

if __name__ == '__main__':
    unittest.main()