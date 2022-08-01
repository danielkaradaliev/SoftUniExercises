from functools import wraps


def tags(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            function_result = func(*args)
            return f"<{tag}>{function_result}</{tag}>"
        return wrapper
    return decorator


@tags("p")
def join_strings(*args):
    return "".join(args)


@tags("h1")
def to_upper(text):
    return text.upper()


print(join_strings("Hello", " you!"))
print(to_upper('hello'))
