class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self, head=None, end=None):
        self.head = head
        self.end = end

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""

        first_node = Node(data)

        if not self.head:
            self.end = first_node

        else:
            first_node.next_node = self.head

        self.head = first_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        last_node = Node(data)

        if self.head is None:
            self.head = last_node
        else:
            self.end.next_node = last_node
        self.end = last_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
