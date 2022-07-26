class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.__current_count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_count < 0:
            raise StopIteration
        value_to_return = self.__current_count
        self.__current_count -= 1
        return value_to_return


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
