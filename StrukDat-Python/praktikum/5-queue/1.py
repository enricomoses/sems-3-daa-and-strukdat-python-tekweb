class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


def time_required_to_buy(tickets, k):
    q = Queue()
    for i in range(len(tickets)):
        q.enqueue([i, tickets[i]])

    time = 0

    while not q.is_empty():
        person = q.dequeue()
        idx = person[0]
        t = person[1]

        time += 1
        t -= 1

        if t == 0:
            if idx == k:
                return time
        else:
            q.enqueue([idx, t])

    return time



print(time_required_to_buy([2, 3, 2], 2))

print(time_required_to_buy([5, 1, 1, 1], 0))