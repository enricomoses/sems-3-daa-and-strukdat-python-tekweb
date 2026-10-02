# 1. Given a linked list, the task is to reverse the linked list by changing the links between nodes.
# Examples:
# Input: Linked List = 1 -> 2 -> 3 -> 4 -> NULL
# Output: Reversed Linked List = 4 -> 3 -> 2 -> 1 -> NULL

# Input: Linked List = 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# Output: Reversed Linked List = 5 -> 4 -> 3 -> 2 -> 1 -> NULL

# Input: Linked List = NULL
# Output: Reversed Linked List = NULL

# Input: Linked List = 1->NULL
# Output: Reversed Linked List = 1->NULL

# Ini buat yang satuan

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Ini buat yang list
class LinkedList:
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
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.reverse()
llist.printList()