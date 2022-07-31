from functools import wraps


def make_bold(func):
    @wraps(func)
    def wrapper(*args):
        result = f"<b>{func(*args)}</b>"
        return result

    return wrapper


def make_italic(func):
    @wraps(func)
    def wrapper(*args):
        result = f"<i>{func(*args)}</i>"
        return result

    return wrapper


def make_underline(func):
    @wraps(func)
    def wrapper(*args):
        result = f"<u>{func(*args)}</u>"
        return result

    return wrapper


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet("Peter"))
print(greet_all("Peter", "George"))
