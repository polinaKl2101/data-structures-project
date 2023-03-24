class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = None


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.items = []
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.tail is None:
            self.head = self.tail = Node(data)

        else:
            self.tail.next_node = Node(data)
            self.tail = self.tail.next_node

    def dequeue(self):
        if self.head is None:
            return None
        queue = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next_node
        return queue

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        if self.head is None:
            return ""
        index = self.head
        while index:
            result.append(index.data)
            index = index.next_node
        return '\n'.join(result)
