n, m = [int(x) for x in input().split()]

numbers = [int(input()) for _ in range(n + m)]
n_set = set(numbers[:n])
m_set = set(numbers[n:])

result_set = n_set.intersection(m_set)
for number in result_set:
    print(number)
