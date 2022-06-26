def get_primary_diagonal_elements(matrix):
    matrix_length = len(matrix)
    return [matrix[x][x] for x in range(matrix_length)]


def get_secondary_diagonal_elements(matrix):
    matrix_length = len(matrix)
    return [matrix[x][matrix_length - x - 1] for x in range(matrix_length)]


n = int(input())
my_matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary_diagonal_elements = get_primary_diagonal_elements(my_matrix)
secondary_diagonal_elements = get_secondary_diagonal_elements(my_matrix)

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal_elements])}. "
      f"Sum: {sum(primary_diagonal_elements)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal_elements])}. "
      f"Sum: {sum(secondary_diagonal_elements)}")
