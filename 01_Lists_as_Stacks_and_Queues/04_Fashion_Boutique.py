class Stack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def peek(self):
        try:
            return self.values[-1]
        except IndexError:
            return None

    def __repr__(self):
        return ", ".join(str(x) for x in self.values)


clothes = Stack()
for x in input().split():
    clothes.push(int(x))
rack_capacity = int(input())
current_rack_capacity_left = rack_capacity
racks = 1 if clothes.peek() is not None else 0

while clothes.values:
    current_item = clothes.pop()
    if current_item <= current_rack_capacity_left:
        current_rack_capacity_left -= current_item
    else:
        racks += 1
        current_rack_capacity_left = rack_capacity - current_item

print(racks)
