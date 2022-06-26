rows = int(input())
my_matrix = []

for row in range(rows):
    my_matrix.append([int(x) for x in input().split()])

row_range = len(my_matrix)
col_range = len(my_matrix[0]) # Assuming we always receive a valid matrix
while True:
    command = input()
    if command == "END":
        for row in my_matrix:
            print(f"{' '.join([str(x) for x in row])}")
        break

    operation, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if row not in range(row_range) or col not in range(col_range):
        print("Invalid coordinates")
        continue

    if operation == "Add":
        my_matrix[row][col] += value
    elif operation == "Subtract":
        my_matrix[row][col] -= value
