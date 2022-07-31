from functools import wraps


def type_check(type_needed):
    def decorator(func):
        @wraps(func)
        def wrapper(param):
            if not isinstance(param, type_needed):
                return "Bad Type"
            result = func(param)
            return result

        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]


print(times2(2))
print(times2('Not A Number'))
print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
