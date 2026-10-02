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

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def display(self):
        temp = self.head
        if not temp:
            print("NULL")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


sll1 = SingleLinkedList()
for val in [1, 2, 3, 4]:
    sll1.insert_at_end(val)
print("Input: Linked List = ", end="")
sll1.display()
sll1.reverse()
print("Output: Reversed Linked List = ", end="")
sll1.display()

print()
sll2 = SingleLinkedList()
for val in [1, 2, 3, 4, 5]:
    sll2.insert_at_end(val)
print("Input: Linked List = ", end="")
sll2.display()
sll2.reverse()
print("Output: Reversed Linked List = ", end="")
sll2.display()

print()
sll3 = SingleLinkedList()
print("Input: Linked List = ", end="")
sll3.display()
sll3.reverse()
print("Output: Reversed Linked List = ", end="")
sll3.display()

print()
sll4 = SingleLinkedList()
sll4.insert_at_end(1)
print("Input: Linked List = ", end="")
sll4.display()
sll4.reverse()
print("Output: Reversed Linked List = ", end="")
sll4.display()