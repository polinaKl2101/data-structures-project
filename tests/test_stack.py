"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
import src.stack
from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_init(self):
        self.assertEqual((Node(5, None)).data, int(5))
        self.assertEqual(self.n2.next_node, self.n2.next_node)


class TestStack(unittest.TestCase):

    exmp = Node(7, None)

    def test_init(self):
        self.assertEqual((Node(5, None)).data, int(5))

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        self.assertEqual((stack.top.data), 'data1')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        data = stack.pop()
        self.assertEqual((stack.top.data), 'data1')


if __name__ == '__main__':
    unittest.main()