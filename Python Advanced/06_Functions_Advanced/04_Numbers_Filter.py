def even_odd_filter(*args, **kwargs):
    def even(*args, **kwargs):
        return [int(x) for x in args if x % 2 == 0]

    def odd(*args, **kwargs):
        return [int(x) for x in args if x % 2 == 1]

    func_map = {
        "odd": odd,
        "even": even
    }

    return dict({k: func_map[k](*v) for k, v in sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True)})


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

