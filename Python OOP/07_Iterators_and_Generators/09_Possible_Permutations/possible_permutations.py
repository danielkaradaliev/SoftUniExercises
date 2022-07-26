def possible_permutations(lst: list):
    from itertools import permutations

    for x in permutations(lst):
        yield list(x)


[print(n) for n in possible_permutations([1, 2, 3])]