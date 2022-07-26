class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.__iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= self.__iterations:
            raise StopIteration
        number_to_return = self.step * self.__iterations
        self.__iterations += 1
        return number_to_return


print("-----------------------")
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print("-----------------------")
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
print("-----------------------")
