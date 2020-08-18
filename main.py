from linked_list.linked_list import LinkedList

linked_list = LinkedList()
linked_list.add(2)
linked_list.add(4)
linked_list.add(25)
linked_list.add(20)
linked_list.add(12)
print(list(linked_list.walk()))

linked_list.remove(20)
print(list(linked_list.walk()))
print(linked_list.head.value, linked_list.tail.value)
