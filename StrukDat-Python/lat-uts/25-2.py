class Queue:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.kapasitas

    def Enqueue(self, item):
        if not self.isFull():
            self.items.append(item)
        else:
            print('Queue is full')

    def Dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            print('Queue is empty')
            return None

    def display(self):
        for i in self.items:
            print(i, end='=>')
        print('end')


def simulasi_permainan(n, k):
    permainan = Queue(n)
    antrian_eliminasi = Queue(n)

    for i in range(1, n+1):
        permainan.Enqueue(i)

    sisa = n

    while sisa > 1:
        for i in range(k):
            peserta = permainan.Dequeue()
            permainan.Enqueue(peserta)

        peserta = permainan.Dequeue()
        antrian_eliminasi.Enqueue(peserta)

        sisa -= 1

    pemenang = permainan.Dequeue()

    eliminasi = ''

    while not antrian_eliminasi.isEmpty():
        if eliminasi != '':
            eliminasi += ', '

        eliminasi += str(antrian_eliminasi.Dequeue())

    return eliminasi, pemenang

if __name__ == '__main__':
    eliminasi, pemenang = simulasi_permainan(7, 3)
    print('Urutan eliminasi:', eliminasi)
    print('Pemenang:', pemenang)