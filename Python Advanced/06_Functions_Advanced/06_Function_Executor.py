def func_executor(*args, **kwargs):
    from os import linesep

    result = []
    for arg in args:
        result.append(f"{arg[0].__name__} - {arg[0](*arg[1])}")

    return linesep.join([str(x) for x in result])


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

