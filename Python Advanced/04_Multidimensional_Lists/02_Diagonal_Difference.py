def get_primary_diagonal_elements(matrix):
    matrix_length = len(matrix)
    return [matrix[x][x] for x in range(matrix_length)]


def get_secondary_diagonal_elements(matrix):
    matrix_length = len(matrix)
    return [matrix[x][matrix_length - x - 1] for x in range(matrix_length)]


n = int(input())
my_matrix = [[int(x) for x in input().split()] for _ in range(n)]
print(abs(sum(get_primary_diagonal_elements(my_matrix)) - sum(get_secondary_diagonal_elements(my_matrix))))
