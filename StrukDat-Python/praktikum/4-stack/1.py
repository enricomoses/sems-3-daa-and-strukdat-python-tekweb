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


def check_balanced(s):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.pop() != pairs[char]:
                return "Unbalanced"

    if stack.is_empty():
        return "Balanced"
    else:
        return "Unbalanced"


print("{[()()][]}")
print(check_balanced("{[()()][]}"))

print("{[(()])}")
print(check_balanced("{[(()])}"))