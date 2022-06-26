DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def get_santa_position(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "S":
                return row_index, col_index


def get_number_of_nice_kids(matrix):
    nice_kids = 0
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "V":
                nice_kids += 1
    return nice_kids


def movement(matrix, x, y, direction):
    """
    Check if the passed coordinates are inside the matrix
    :param matrix: matrix
    :param x: x
    :param y: y
    :return: Return True and new coordinates if movement inside matrix,
    otherwise return False and the original same coordinates (stay on the same position)
    """
    matrix_length = len(matrix)
    new_x = x + DIRECTIONS[direction][0]
    new_y = y + DIRECTIONS[direction][1]
    if new_x not in range(matrix_length) or new_y not in range(matrix_length):
        return False, x, y
    return True, new_x, new_y


number_of_presents = int(input())
neighbourhood_size = int(input())
neighbourhood = []

for _ in range(neighbourhood_size):
    neighbourhood.append([x for x in input().split()])

santa_x, santa_y = get_santa_position(neighbourhood)
number_of_nice_kids = get_number_of_nice_kids(neighbourhood)
number_of_nice_kids_remaining = number_of_nice_kids

while True:
    command = input()
    if command == "Christmas morning":
        break
    direction = command
    movement_successful, new_x, new_y = movement(neighbourhood, santa_x, santa_y, direction)
    if movement_successful:
        symbol = neighbourhood[new_x][new_y]
        if symbol == "V":
            number_of_presents -= 1
            number_of_nice_kids_remaining -= 1
        elif symbol == "C":
            for direction, coordinates in DIRECTIONS.items():
                cookie_x, cookie_y = new_x + coordinates[0], new_y + coordinates[1]
                if neighbourhood[cookie_x][cookie_y] == "V":
                    number_of_presents -= 1
                    number_of_nice_kids_remaining -= 1
                    neighbourhood[cookie_x][cookie_y] = "-"
                elif neighbourhood[cookie_x][cookie_y] == "X":
                    number_of_presents -= 1
                    neighbourhood[cookie_x][cookie_y] = "-"

        neighbourhood[santa_x][santa_y] = "-"
        santa_x, santa_y = new_x, new_y
        neighbourhood[santa_x][santa_y] = "S"

    if number_of_presents == 0:
        break

if number_of_presents == 0 and number_of_nice_kids_remaining > 0:
    print("Santa ran out of presents!")

for row in neighbourhood:
    print(f"{' '.join(row)}")

if number_of_nice_kids_remaining == 0:
    print(f"Good job, Santa! {number_of_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {number_of_nice_kids_remaining} nice kid/s.")
