number = int(input())
even_set = set()
odd_set = set()

for current_row in range(1, number + 1):
    name = input()
    current_number = sum(ord(char) for char in name) // current_row
    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

even_set_sum = sum(even_set)
odd_set_sum = sum(odd_set)

if even_set_sum == odd_set_sum:
    print(", ".join([str(x) for x in even_set.union(odd_set)]))
elif odd_set_sum > even_set_sum:
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
else:
    print(", ".join([str(x) for x in even_set.symmetric_difference(odd_set)]))
