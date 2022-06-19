from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups_of_milk = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while True:
    if milkshakes >= 5:
        break
    if len(chocolates) == 0 or len(cups_of_milk) == 0:
        break
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue
    if chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolates):
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if len(cups_of_milk):
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
