def fibonacci():
    yield 0
    yield 1
    last_number = 0
    current_number = 1
    while True:
        yield last_number + current_number
        last_number, current_number = current_number, last_number + current_number


generator = fibonacci()
for i in range(10):
    print(next(generator))
