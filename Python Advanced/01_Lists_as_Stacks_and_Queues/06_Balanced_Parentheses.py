class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        self.values.pop()

    def peek(self):
        return self.values[-1]

    def __bool__(self):
        return bool(self.values)

    def __repr__(self):
        return ", ".join(self.values)


expression = input()
brackets = Stack()
opening_brackets = ("(", "[", "{")
closing_brackets = (")", "]", "}")

for char in expression:
    if char in opening_brackets:
        brackets.push(char)
    elif char in closing_brackets:
        if not brackets:
            # Push the closing bracket to the stack, so it's not empty and confuse the final if check
            brackets.push(char)
            break
        if brackets.peek() == opening_brackets[closing_brackets.index(char)]:
            brackets.pop()

if brackets:
    print("NO")
else:
    print("YES")
