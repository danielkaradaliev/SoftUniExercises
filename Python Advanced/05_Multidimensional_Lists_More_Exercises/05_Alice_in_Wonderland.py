def get_alice_position(matrix):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == "A":
                return row_index, col_index


size = int(input())
my_matrix = []
tea_bags = 0
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(size):
    my_matrix.append([x for x in input().split()])

current_row, current_col = get_alice_position(my_matrix)
my_matrix[current_row][current_col] = "*"

while True:
    command = input()

    current_row += moves[command][0]
    current_col += moves[command][1]

    if current_row not in range(size) or current_col not in range(size):
        print("Alice didn't make it to the tea party.")
        break

    position_value = my_matrix[current_row][current_col]
    my_matrix[current_row][current_col] = "*"

    if position_value == "R":
        print("Alice didn't make it to the tea party.")
        break

    if position_value in {".", "*"}:
        continue

    tea_bags += int(position_value)
    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break

for row in my_matrix:
    print(f"{' '.join(row)}")
