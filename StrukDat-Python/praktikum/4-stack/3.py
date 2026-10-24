class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


def sort_array(arr):
    input_stack = Stack()
    temp_stack = Stack()

    for num in arr:
        input_stack.push(num)

    while not input_stack.is_empty():
        temp = input_stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() < temp:
            input_stack.push(temp_stack.pop())

        temp_stack.push(temp)

    sorted_arr = []
    while not temp_stack.is_empty():
        sorted_arr.append(temp_stack.pop())

    return sorted_arr


arr = [3, 1, 4, 2]
print(arr)

print(sort_array(arr))