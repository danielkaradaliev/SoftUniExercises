def get_primes(lst: list):
    def is_prime(k):
        if k == 2 or k == 3: return True
        if k % 2 == 0 or k < 2: return False
        for i in range(3, int(k ** 0.5) + 1, 2):
            if k % i == 0:
                return False

        return True

    for number in [x for x in lst if is_prime(x)]:
        yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
