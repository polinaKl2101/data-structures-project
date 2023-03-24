"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
import src.queue
from src.queue import Node, Queue


class TestNode(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_init(self):
        self.assertEqual((Node(5, None)).data, int(5))
        self.assertEqual(self.n2.next_node, self.n2.next_node)


class TestStack(unittest.TestCase):

    def test_init(self):
        self.assertEqual((Node(5, None)).data, int(5))

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), 'data3')
        self.assertEqual(queue.dequeue(), None)

    def test_str(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), "data1\ndata2\ndata3")


if __name__ == '__main__':
    unittest.main()