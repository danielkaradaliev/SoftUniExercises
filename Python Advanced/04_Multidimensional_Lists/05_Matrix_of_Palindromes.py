rows, columns = [int(x) for x in input().split()]
my_matrix = []

for row_index in range(rows):
    ordinal = 97 + row_index
    my_matrix.append(["".join([chr(ordinal), chr(ordinal + col_index), chr(ordinal)]) for col_index in range(columns)])

for row in my_matrix:
    print(f"{' '.join(row)}")
