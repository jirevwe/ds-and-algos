from ds.linked_list.linked_list import LinkedList

linkedList = LinkedList()
linkedList.add(2)
linkedList.add(4)
linkedList.add(25)
linkedList.add(20)
linkedList.add(12)
print(list(linkedList.walk()))

linkedList.remove(20)
print(list(linkedList.walk()))
print(linkedList.head.value, linkedList.tail.value)
