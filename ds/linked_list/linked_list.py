from ds.node.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head.value

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, value):
        if self.head is None:
            return False

        current = self.head
        if current.value == value:
            if self.head.value == self.tail.value:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return True

        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            if current.next.value == self.tail.value:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def walk(self):
        node = self.head
        while node is not None:
            yield node.value
            node = node.next
