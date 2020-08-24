from linked_list.linked_list import LinkedList
from node.node import Node


class DoublyLinkedList(LinkedList):
    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head.previous = node
        self.head = node

    def remove(self, value):
        if self.head is None:
            return False

        current = self.head
        if current.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.previous = None
            return True

        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            if current.next == self.tail:
                self.tail = current
                self.tail.next = None
            else:
                current.next.next.previous = current
                current.next = current.next.next
            return True
        return False

    def walk_reverse(self):
        node = self.tail
        items = []
        while node is not None:
            items.append(node.value)
            node = node.previous
        return items
