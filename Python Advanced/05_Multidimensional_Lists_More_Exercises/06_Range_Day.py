DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def get_shooter_position(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "A":
                return row_index, col_index


def get_number_of_targets(matrix):
    total_targets = 0
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "x":
                total_targets += 1
    return total_targets


def valid_movement(matrix, row, col):
    matrix_length = len(matrix)
    if row not in range(matrix_length) or col not in range(matrix_length) or matrix[row][col] != ".":
        return False
    return True


def target_shot(matrix, row, col, direction):
    matrix_length = len(matrix)
    x = row
    y = col
    while True:
        x, y = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
        if x not in range(matrix_length) or y not in range(matrix_length):
            break
        if matrix[x][y] == "x":
            return True, x, y
    return False, None, None


size = 5
my_matrix = []
targets_shot = []

for _ in range(size):
    my_matrix.append([x for x in input().split()])

number_of_commands = int(input())
shooter_position_x, shooter_position_y = get_shooter_position(my_matrix)
targets = get_number_of_targets(my_matrix)

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        direction, steps = command[1:]
        intended_x = shooter_position_x + (DIRECTIONS[direction][0] * int(steps))
        intended_y = shooter_position_y + (DIRECTIONS[direction][1] * int(steps))

        if not valid_movement(my_matrix, intended_x, intended_y):
            continue

        my_matrix[shooter_position_x][shooter_position_y] = "."
        shooter_position_x, shooter_position_y = intended_x, intended_y
        my_matrix[shooter_position_x][shooter_position_y] = "A"

    elif command[0] == "shoot":
        direction = command[1]
        shooting_successful, x, y = target_shot(my_matrix, shooter_position_x, shooter_position_y, direction)
        if shooting_successful:
            targets -= 1
            targets_shot.append([x, y])
            my_matrix[x][y] = "."

if targets == 0:
    print(f"Training completed! All {len(targets_shot)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

for target in targets_shot:
    print(target)
