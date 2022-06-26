class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def remove(self):
        try:
            self.values.pop()
        except IndexError:
            pass

    def print_max_value(self):
        try:
            print(max(self.values))
        except ValueError:
            pass

    def print_min_value(self):
        try:
            print(min(self.values))
        except ValueError:
            pass

    def print_stack(self):
        return ", ".join([str(x) for x in self.values[::-1]])

    def __repr__(self):
        return ", ".join([str(x) for x in self.values])


stack = Stack()
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == "1":
        stack.push(int(command[1]))
    elif command[0] == "2":
        stack.remove()
    elif command[0] == "3":
        stack.print_max_value()
    elif command[0] == "4":
        stack.print_min_value()

print(stack.print_stack())
