class sequence_repeat:
    def __init__(self, sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.__iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iteration >= self.number:
            raise StopIteration
        index = self.__iteration % len(self.sequence)
        self.__iteration += 1
        return self.sequence[index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
