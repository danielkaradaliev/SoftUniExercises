class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iteration >= len(self.dictionary):
            raise StopIteration
        kv_pair_to_return = list(self.dictionary.items())[self.__iteration]
        self.__iteration += 1
        return kv_pair_to_return


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
