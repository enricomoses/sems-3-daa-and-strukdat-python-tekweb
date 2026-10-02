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

    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()
        curr = self.head
        while curr:
            if curr.data in seen:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            else:
                seen.add(curr.data)
            curr = curr.next

    def display(self):
        temp = self.head
        while temp:
            if temp.next:
                print(temp.data, end="<->")
            else:
                print(temp.data)
            temp = temp.next


dll1 = DoubleLinkedList()
for val in [8, 4, 4, 6, 4, 8, 4, 10, 12, 12]:
    dll1.insert_at_end(val)

print("Input: ", end="")
dll1.display()

dll1.remove_duplicates()

print("Output: ", end="")
dll1.display()