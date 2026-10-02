class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def merge_sorted(self, other_list):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other_list.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b
        self.head = dummy.next
        other_list.head = None

    def display(self):
        temp = self.head
        if not temp:
            print("null")
            return
        while temp:
            if temp.next:
                print(temp.data, end="->")
            else:
                print(temp.data, end="")
            temp = temp.next
        print()


print()
list_a1 = SingleLinkedList()
for val in [5, 10, 15]:
    list_a1.insert_at_end(val)
list_b1 = SingleLinkedList()
for val in [2, 3, 20]:
    list_b1.insert_at_end(val)

list_a1.display()
list_b1.display()

list_a1.merge_sorted(list_b1)

list_a1.display()

print()
list_a2 = SingleLinkedList()
list_a2.insert_at_end(1)
list_a2.insert_at_end(1)
list_b2 = SingleLinkedList()
list_b2.insert_at_end(2)
list_b2.insert_at_end(4)

list_a2.display()
list_b2.display()

list_a2.merge_sorted(list_b2)

list_a2.display()

print()
list_a3 = SingleLinkedList()
for val in [1, 2, 3]:
    list_a3.insert_at_end(val)
list_b3 = SingleLinkedList()

list_a3.display()
list_b3.display()

list_a3.merge_sorted(list_b3)

list_a3.display()