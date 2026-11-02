class Node:
    def __init__(self, nama_tugas, prioritas):
        self.nama_tugas = nama_tugas
        self.prioritas = prioritas
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addLast(self, nama_tugas, prioritas):
        new_node = Node(nama_tugas, prioritas)

        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def display(self):
        cur = self.head

        while cur:
            print(f'{cur.nama_tugas} : {cur.prioritas}', end=' -> ')
            cur = cur.next

        print('None')

    def hapus_prioritas(self, node, batas):
        if node is None:
            return None

        node.next = self.hapus_prioritas(node.next, batas)

        if node.prioritas > batas:
            return node.next

        return node

linkedList = LinkedList()

linkedList.addLast('Coding', 2)
linkedList.addLast('Gaming', 5)
linkedList.addLast('Makan', 3)
linkedList.addLast('Tidur', 7)

linkedList.display()

linkedList.head = linkedList.hapus_prioritas(linkedList.head, 4)

linkedList.display()