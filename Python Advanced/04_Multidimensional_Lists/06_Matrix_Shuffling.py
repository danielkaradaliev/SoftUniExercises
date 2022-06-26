def validate_coordinate(matrix, coordinates):
    matrix_row_length = len(matrix)
    matrix_col_length = len(matrix[0])
    for coordinate in coordinates:
        row, col = coordinate
        if row not in range(0, matrix_row_length) or col not in range(0, matrix_col_length):
            return False
    return True


rows, columns = [int(x) for x in input().split()]
my_matrix = []

for row_index in range(rows):
    my_matrix.append([x for x in input().split()])

while True:
    command = input()
    if command == "END":
        break
    command_breakdown = command.split()
    if command_breakdown[0] != "swap" or len(command_breakdown) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command_breakdown[1:]]
    coordinates = ((row1, col1), (row2, col2))
    if not validate_coordinate(my_matrix, coordinates):
        print("Invalid input!")
        continue

    my_matrix[row1][col1], my_matrix[row2][col2] = my_matrix[row2][col2], my_matrix[row1][col1]
    for row in my_matrix:
        print(f"{' '.join(row)}")
