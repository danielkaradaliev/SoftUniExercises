from functools import wraps


class store_results:
    __log_path = "./results.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        linesep = "\n"
        function_result = self.func(*args, **kwargs)
        with open(self.__log_path, "a") as log_file:
            log_file.write(f"Function '{self.func.__name__}' was called. Result: {function_result}{linesep}")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
