def is_square_matrix(matrix, row_index, col_index):
    if matrix[row_index][col_index] == matrix[row_index + 1][col_index] == \
       matrix[row_index][col_index + 1] == matrix[row_index + 1][col_index + 1]:
        return True
    return False


rows, columns = [int(x) for x in input().split()]
my_matrix = [input().split() for y in range(rows)]
square_matrices = 0

for r_index in range(rows - 1):
    for c_index in range(columns - 1):
        if is_square_matrix(my_matrix, r_index, c_index):
            square_matrices += 1

print(square_matrices)
