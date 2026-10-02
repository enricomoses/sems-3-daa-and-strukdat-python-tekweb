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

    def merge_alternate(self, other_list):
        p_curr = self.head
        q_curr = other_list.head

        while p_curr and q_curr:
            p_next = p_curr.next
            q_next = q_curr.next

            p_curr.next = q_curr
            q_curr.next = p_next

            p_curr = p_next
            q_curr = q_next

        other_list.head = q_curr

    def display(self):
        temp = self.head
        if not temp:
            print("empty")
            return
        while temp:
            if temp.next:
                print(temp.data, end="->")
            else:
                print(temp.data, end="")
            temp = temp.next
        print()


list1_1 = SingleLinkedList()
for val in [5, 7, 17, 13, 11]:
    list1_1.insert_at_end(val)
list2_1 = SingleLinkedList()
for val in [12, 10, 2, 4, 6]:
    list2_1.insert_at_end(val)

list1_1.display()
list2_1.display()

list1_1.merge_alternate(list2_1)

list1_1.display()
list2_1.display()

print()
list1_2 = SingleLinkedList()
for val in [1, 2, 3]:
    list1_2.insert_at_end(val)
list2_2 = SingleLinkedList()
for val in [4, 5, 6, 7, 8]:
    list2_2.insert_at_end(val)

list1_2.display()
list2_2.display()

list1_2.merge_alternate(list2_2)

list1_2.display()
list2_2.display()