def collect_eggs(matrix, row, col):
    result = []
    matrix_length = len(matrix)
    moves = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    for move, coordinates in moves.items():
        eggs = 0
        moves_made = []
        new_x = row
        new_y = col
        while True:
            new_x, new_y = new_x + coordinates[0], new_y + coordinates[1]
            if new_x not in range(matrix_length) or new_y not in range(matrix_length) or matrix[new_x][new_y] == "X":
                break
            eggs += int(matrix[new_x][new_y])
            moves_made.append([new_x, new_y])
        result.append((move, moves_made, eggs))

    return sorted(result, key=lambda x: x[2], reverse=True)


def find_bunny_coordinates(matrix):
    for row_index, row in enumerate(my_matrix):
        for col_index, col in enumerate(row):
            if my_matrix[row_index][col_index] == "B":
                return row_index, col_index


field_size = int(input())
my_matrix = []
eggs_collected = []

for _ in range(field_size):
    my_matrix.append([x for x in input().split()])

bunny_coordinate_x, bunny_coordinate_y = find_bunny_coordinates(my_matrix)
eggs_collected = collect_eggs(my_matrix, bunny_coordinate_x, bunny_coordinate_y)
best_result = eggs_collected[0]
print(best_result[0])
for coordinate in best_result[1]:
    print(coordinate)
print(best_result[2])
