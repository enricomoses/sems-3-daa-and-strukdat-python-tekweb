class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def count_students_unable_to_eat(students, sandwiches):
    student_q = Queue()
    for s in students:
        student_q.enqueue(s)

    rotations = 0

    while not student_q.is_empty() and rotations < student_q.size():
        if student_q.peek() == sandwiches[0]:
            student_q.dequeue()
            sandwiches.pop(0)
            rotations = 0
        else:
            student_q.enqueue(student_q.dequeue())
            rotations += 1

    return student_q.size()


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
print(count_students_unable_to_eat(students, sandwiches))