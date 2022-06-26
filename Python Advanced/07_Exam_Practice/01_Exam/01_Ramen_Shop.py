from collections import deque

bowls_of_ramen = deque([int(x) for x in input().split(", ")])
customers = deque([int(x) for x in input().split(", ")])

while True:
    ramen_value = bowls_of_ramen.pop()
    customer = customers.popleft()
    if ramen_value > customer:
        bowls_of_ramen.append(ramen_value - customer)
    elif customer > ramen_value:
        customers.appendleft(customer - ramen_value)

    if not len(customers):
        print("Great job! You served all the customers.")
        if len(bowls_of_ramen):
            print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
        break
    elif not len(bowls_of_ramen):
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join([str(x) for x in customers])}")
        break
