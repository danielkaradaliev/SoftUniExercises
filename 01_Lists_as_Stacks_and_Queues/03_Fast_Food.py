from collections import deque

orders = deque()
biggest_order = 0
food_quantity_for_the_day = int(input())
sequence = input().split()
for number in sequence:
    food_quantity = int(number)
    if food_quantity > biggest_order:
        biggest_order = food_quantity
    orders.append(food_quantity)

print(biggest_order)

while orders:
    if food_quantity_for_the_day >= orders[0]:
        food_quantity_for_the_day -= orders.popleft()
    else:
        break
if not orders:
    print("Orders complete")
else:
    print("Orders left: ", end="")
    while orders:
        print(orders.popleft(), end=" ")
