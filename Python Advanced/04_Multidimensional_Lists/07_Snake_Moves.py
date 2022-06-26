rows, columns = [int(x) for x in input().split()]
snake = input()
my_matrix = []
counter = 0

for row in range(rows):
    my_matrix.append([])
    for col in range(columns):
        my_matrix[row].append(snake[counter % len(snake)])
        counter += 1
    if row % 2 == 1:
        my_matrix[row].reverse()

for row in my_matrix:
    print(f"{''.join(row)}")
