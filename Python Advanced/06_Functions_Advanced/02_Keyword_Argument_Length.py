def kwargs_length(*args, **kwargs):
    return len(kwargs)


dictionary = {}

print(kwargs_length(**dictionary))
