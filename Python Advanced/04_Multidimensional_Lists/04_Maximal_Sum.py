def get_submatrix(matrix, row_index, col_index, square_dimension):
    submatrix = []
    for x in range(row_index, row_index + square_dimension):
        submatrix.append([matrix[x][y] for y in range(col_index, col_index + square_dimension)])
    return submatrix


def sum_matrix(matrix):
    return sum([sum(x) for x in matrix])


rows, columns = [int(x) for x in input().split()]
my_matrix = [[int(x) for x in input().split()] for y in range(rows)]
square_dimension = 3
all_submatrices = [get_submatrix(my_matrix, r, c, square_dimension) for
                   r in range(rows - square_dimension + 1) for c in range(columns - square_dimension + 1)]
all_submatrices.sort(key=lambda x: sum_matrix(x), reverse=True)

print(f"Sum = {sum_matrix(all_submatrices[0])}")
for row in all_submatrices[0]:
    print(f"{' '.join([str(x) for x in row])}")
