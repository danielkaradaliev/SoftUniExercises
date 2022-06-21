def is_square_matrix(matrix, row_index, col_index, square_dimension):
    symbol = matrix[row_index][col_index]
    for r in range(row_index, row_index + square_dimension):
        for c in range(col_index, col_index + square_dimension):
            if matrix[r][c] != symbol:
                return False
    return True


rows, columns = [int(x) for x in input().split()]
my_matrix = [input().split() for y in range(rows)]
square_dimension = 2
square_matrices = 0

for r_index in range(rows - square_dimension + 1):
    for c_index in range(columns - square_dimension + 1):
        if is_square_matrix(my_matrix, r_index, c_index, square_dimension):
            square_matrices += 1

print(square_matrices)
