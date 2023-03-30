"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
import src.linked_list
from src.linked_list import Node, LinkedList


class TestNode(unittest.TestCase):
    data1 = Node(1, None)

    def test_init(self):
        self.assertEqual(Node(1).data, int(1))
        self.assertEqual(self.data1.next_node, self.data1.next_node)


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning_first(self):
        example_one = LinkedList()
        example_one.insert_beginning({'id': 1})
        self.assertEqual(example_one.head.data, {'id': 1})
        self.assertEqual(example_one.end.data, {'id': 1})

    def test_insert_beginning_second(self):
        example_two = LinkedList()
        example_two.insert_beginning({'id': 1})
        example_two.insert_beginning({'id': 5})
        self.assertEqual(example_two.head.data, {'id': 5})
        self.assertEqual(example_two.end.data, {'id': 1})

    def test_insert_at_end_first(self):
        example_three = LinkedList()
        example_three.insert_at_end({'id': 1})
        example_three.insert_at_end({'id': 3})
        self.assertEqual(example_three.head.data, {'id': 1})
        self.assertEqual(example_three.end.data, {'id': 3})

