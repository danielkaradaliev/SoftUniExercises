from collections import deque


def multiply_values(values):
    product = values.popleft()
    while values:
        product *= values.popleft()
    return deque([product])


def sum_values(values):
    sum_of_values = values.popleft()
    while values:
        sum_of_values += values.popleft()
    return deque([sum_of_values])


def subtract_values(values):
    difference = values.popleft()
    while values:
        difference -= values.popleft()
    return deque([difference])


def divide_values(values):
    quotient = values.popleft()
    while values:
        quotient //= values.popleft()
    return deque([quotient])


expression = input().split()
result = deque()

for symbol in expression:
    if symbol == "*":
        result = multiply_values(result)
    elif symbol == "+":
        result = sum_values(result)
    elif symbol == "-":
        result = subtract_values(result)
    elif symbol == "/":
        result = divide_values(result)
    else:
        result.append(int(symbol))

print(result.popleft())
