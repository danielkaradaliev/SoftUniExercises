from functools import wraps


def only_even(*args):
    for x in args:
        if not isinstance(x, int) or x % 2 == 1:
            return False
    return True


def even_parameters(func):
    @wraps(func)
    def wrapper(*args):
        if not only_even(*args):
            return "Please use only even numbers!"
        result = func(*args)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(add(2, 4))
print(add("Peter", 1))

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
