DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


def get_rover_position(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "E":
                return row_index, col_index


def movement(matrix, x, y, direction):
    matrix_length = len(matrix)

    new_x = (x + DIRECTIONS[direction][0]) % matrix_length
    new_y = (y + DIRECTIONS[direction][1]) % matrix_length

    return new_x, new_y


field_span = 6
field = []
deposits = {
    "Water": 0,
    "Metal": 0,
    "Concrete": 0
}
deposits_map = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete"
}

for _ in range(field_span):
    field.append([x for x in input().split()])

rover_x, rover_y = get_rover_position(field)

commands = input().split(", ")

for command in commands:
    rover_x, rover_y = movement(field, rover_x, rover_y, command)
    symbol = field[rover_x][rover_y]
    if symbol == "R":
        print(f"Rover got broken at ({rover_x}, {rover_y})")
        break
    elif symbol in ("W", "M", "C"):
        deposits[deposits_map[symbol]] += 1
        print(f"{deposits_map[symbol]} deposit found at ({rover_x}, {rover_y})")

if all([x > 0 for x in deposits.values()]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
