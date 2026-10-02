class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        else:
            i = 1
            cur = self.head
            while i < position:
                if cur.next == None:
                    print("Posisi Tidak Valid")
                    return
                cur = cur.next
                i += 1
            new_node.next = cur.next
            cur.next = new_node

    def delete_at_position(self, position):
        if not self.head:
            print("Linked List Kosong")
        else:
            cur = self.head
            if position == 0:
                self.head = cur.next
                cur = None
                return
            else:
                i = 1
                cur = self.head
                while i < position:
                    if cur.next == None:
                        print("Posisi Tidak Valid")
                        return
                    cur = cur.next
                    i += 1
                if cur.next == None:
                    print("Posisi Tidak Valid")
                    return
                temp = cur.next
                cur.next = cur.next.next
                temp = None




    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

if __name__ == "__main__":
    antre = LinkedList()

    while True:
        print("""===== ANTRIAN PEMBELI =====
1. Tambah Pembeli di Awal
2. Tambah Pembeli di Akhir
3. Tambah Pembeli pada Posisi Tertentu
4. Hapus Pembeli pada Posisi Tertentu
5. Tampilkan Antrian
6. Keluar
        """)

        pilihan = int(input("Masukkan Pilihan: "))

        if pilihan == 1:
            nama = input("Masukkan Nama Pembeli: ")
            antre.insert_at_position(nama, 0)
        elif pilihan == 2:
            nama = input("Masukkan Nama Pembeli: ")
            antre.append(nama)
        elif pilihan == 3:
            nama = input("Masukkan Nama Pembeli: ")
            posisi = int(input("Masukkan Posisi: "))
            antre.insert_at_position(nama, posisi)
        elif pilihan == 4:
            posisi = int(input("Masukkan Posisi: "))
            antre.delete_at_position(posisi)
        elif pilihan == 5:
            antre.display()
        elif pilihan == 6:
            break
        else:
            print("Input Tidak Valid")