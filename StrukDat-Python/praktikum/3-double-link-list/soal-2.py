class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
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
        new_node.prev = temp

    def reverse(self):
        curr = self.head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("NULL")


dll2 = DoubleLinkedList()
for val in [1, 2, 3]:
    dll2.insert_at_end(val)

print("Input: ", end="")
dll2.display()

dll2.reverse()

print("Output: ", end="")
dll2.display()