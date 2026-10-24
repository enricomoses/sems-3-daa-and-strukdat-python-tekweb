class CustomPriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if item not in self.items:
            self.items.append(item)
            self.items.sort()

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


def priority_queue_3_numbers():
    user_input = input("Input: ")
    numbers = [int(x) for x in user_input.split()]

    pq = CustomPriorityQueue()

    for num in numbers:
        pq.enqueue(num)

    result = []
    while not pq.is_empty():
        result.append(pq.dequeue())

    print("Output:", " ".join(map(str, result)))

priority_queue_3_numbers()