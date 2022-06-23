def even_odd(*args, **kwargs):
    def even(*args, **kwargs):
        return [x for x in args if x % 2 == 0]

    def odd(*args, **kwargs):
        return [x for x in args if x % 2 == 1]

    func_map = {
        "odd": odd,
        "even": even
    }

    command = args[-1]
    numbers = [int(x) for x in args[:-1]]

    return func_map[command](*numbers)


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
