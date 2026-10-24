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


def browser_history_simulation(commands):
    history = Stack()

    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "visit":
            website = parts[1]
            history.push(website)
        elif action == "back":
            history.pop()
        elif action == "current":
            curr = history.peek()
            if curr:
                print(curr)
            else:
                print("No current page")
        elif action == "exit":
            break


commands = [
    "visit google.com",
    "visit youtube.com",
    "visit github.com",
    "back",
    "current",
    "visit openai.com",
    "back",
    "back",
    "current",
    "exit"
]

browser_history_simulation(commands)