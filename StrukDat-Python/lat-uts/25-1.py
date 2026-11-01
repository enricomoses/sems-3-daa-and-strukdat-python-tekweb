class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self):
        return len(self.items) == 0


def push_ascending(stack, data):
    temp = Stack()

    while not stack.isEmpty() and stack.peek() > data:
        temp.push(stack.pop())

    stack.push(data)

    while not temp.isEmpty():
        stack.push(temp.pop())


def tampilkan(stack):
    temp = Stack()

    while not stack.isEmpty():
        temp.push(stack.pop())

    while not temp.isEmpty():
        data = temp.pop()
        print(data, end=' ')
        stack.push(data)

    print()

stack = Stack()

n = int(input('Jumlah data: '))

for i in range(n):
    angka = int(input('Masukkan angka: '))
    push_ascending(stack, angka)

print('Hasil Stack Ascending: ')
tampilkan(stack)