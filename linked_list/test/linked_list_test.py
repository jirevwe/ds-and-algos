import unittest

from linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list.head, None)
        self.assertEqual(linked_list.tail, None)

    def test_head_is_not_empty(self):
        linked_list = LinkedList()
        linked_list.add(1)
        self.assertEqual(linked_list.head.value, 1)

    def test_node_value_exists(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(22)
        self.assertEqual(linked_list.head.next.value, 22)

    def test_prepend_before_head(self):
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.prepend(20)
        self.assertEqual(linked_list.head.value, 20)

    def test_item_removal(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        linked_list.remove(25)
        self.assertEqual(list(linked_list.walk()), [2, 4, 20, 12])

    def test_walk_list(self):
        linked_list = LinkedList()
        linked_list.add(2)
        linked_list.add(4)
        linked_list.add(25)
        linked_list.add(20)
        linked_list.add(12)
        self.assertEqual(list(linked_list.walk()), [2, 4, 25, 20, 12])
