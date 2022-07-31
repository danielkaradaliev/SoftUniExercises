from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args):
        linesep = "\n"
        result = f"you called {func.__name__}({', '.join([str(x) for x in args])}){linesep}it returned {func(*args)}"
        return result

    return wrapper


@logged
def funcky(*args):
    return 3 + len(args)


@logged
def sum_func(a, b):
    return a + b


print(funcky(4, 4, 4))
print(sum_func(1, 4))
