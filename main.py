from doubly_linked_list.doubly_linked_list import DoublyLinkedList

linked_list = DoublyLinkedList()
linked_list.add(2)
linked_list.add(4)
linked_list.add(25)
linked_list.add(20)
linked_list.add(12)
print(linked_list.walk())

linked_list.remove(20)
print(linked_list.walk())
print(linked_list.head.next.value, linked_list.tail.previous.value)
