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

    def rotate(self, n):
        if n == 0 or not self.head:
            return

        curr = self.head
        count = 1
        while count < n and curr:
            curr = curr.next
            count += 1

        if not curr or not curr.next:
            return

        nth_node = curr

        while curr.next:
            curr = curr.next

        curr.next = self.head
        self.head.prev = curr

        self.head = nth_node.next
        self.head.prev = None
        nth_node.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="  ")
            temp = temp.next
        print()


dll3_1 = DoubleLinkedList()
for val in ['a', 'b', 'c', 'd', 'e']:
    dll3_1.insert_at_end(val)

print("Input : ", end="")
dll3_1.display()
print("N = 2")

dll3_1.rotate(2)

print("Output : ", end="")
dll3_1.display()

print()

dll3_2 = DoubleLinkedList()
for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    dll3_2.insert_at_end(val)

print("Input : ", end="")
dll3_2.display()
print("N = 4")

dll3_2.rotate(4)

print("Output : ", end="")
dll3_2.display()