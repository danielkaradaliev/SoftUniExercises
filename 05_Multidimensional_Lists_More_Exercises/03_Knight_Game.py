def knight_hits(matrix, row, col):
    knight_moves = {(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)}
    hits = 0
    matrix_length = len(matrix)
    for move in knight_moves:
        new_row_index = row + move[0]
        new_col_index = col + move[1]
        if new_row_index not in range(matrix_length) or new_col_index not in range(matrix_length):
            continue
        if matrix[new_row_index][new_col_index] == "K":
            hits += 1

    return hits


matrix_dimension = int(input())
my_matrix = []
knights_removed = 0
for _ in range(matrix_dimension):
    my_matrix.append([x for x in input()])

while True:
    number_of_hits = 0
    most_hits_row = 0
    most_hits_col = 0
    for row_index, row in enumerate(my_matrix):
        for col_index, col in enumerate(row):
            if col == "K":
                current_knight_hits = knight_hits(my_matrix, row_index, col_index)
                if current_knight_hits > number_of_hits:
                    number_of_hits = current_knight_hits
                    most_hits_row = row_index
                    most_hits_col = col_index

    # Remove knight with most hits
    if number_of_hits > 0:
        my_matrix[most_hits_row][most_hits_col] = "0"
        knights_removed += 1
        continue
    break

print(knights_removed)
