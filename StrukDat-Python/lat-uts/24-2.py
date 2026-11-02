class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.next = None

class MemoryManager:
    def __init__(self):
        self.head = None

    def allocate(self, size):
        new_block = MemoryBlock(size)

        if self.head is None:
            self.head = new_block
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_block

    def delloacate(self, size):
        if self.head is None:
            return

        if self.head.size == size:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.size == size:
                prev.next = current.next
                return

            prev = current
            current = current.next

    def print_memory(self):
        current = self.head

        while current is not None:
            print('Block Size:', current.size, end=' -> ')
            current = current.next

        print('None')

    def total_allocated_memory(self):
        total = 0
        current = self.head

        while current is not None:
            total += current.size
            current = current.next

        return total

    def merge_adjacent(self):
        current = self.head

        while current is not None and current.next is not None:
            if current.size == current.next.size:
                current.size += current.next.size
                current.next = current.next.next
            else:
                current = current.next

memory = MemoryManager()

memory.allocate(10)
memory.allocate(10)
memory.allocate(10)
memory.allocate(20)
memory.allocate(30)

print('Memory blocks before dealocating:')
memory.print_memory()

memory.delloacate(10)

print("Memory blocks after dealocating:")
memory.print_memory()

print("Memory blocks before merging:")
memory.print_memory()

memory.merge_adjacent()

print("Memory blocks after merging:")
memory.print_memory()

total_memory = memory.total_allocated_memory()
print(f"Total allocated memory: {total_memory}")
