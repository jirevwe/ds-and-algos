from node.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def add(self, value):
        """
        Adds the value to the end of the list

        :param value: the value to be added
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def prepend(self, value):
        """
        Adds the value to the start of the list

        :param value: the value to be added
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, value):
        """
        Finds the vales and removes it

        :param value: the value to be removed
        :return: True if the value was removed, False if the value isn't in the list
        """
        if self.head is None:
            return False

        current = self.head
        if current.value == value:
            if self.head == self.tail:
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
        """
        Prints out all the items in the list starting from the head

        :rtype: collections.Iterable[Node]
        :returns: An array of the items in the list
        """
        node = self.head
        items = []
        while node is not None:
            items.append(node.value)
            node = node.next
        return items

    def search(self, value):
        """
        Searches the list to see if an item is inside

        :param value: The item searched for
        :returns: True or False
        """
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        if node is None:
            return False
        return True
