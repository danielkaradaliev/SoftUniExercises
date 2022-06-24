def words_sorting(*args, **kwargs):
    from os import linesep

    def ascii_sum(input_word):
        return sum([ord(x) for x in input_word])

    words_dict = dict({word: ascii_sum(word) for word in args})
    sum_of_all_dict_values = sum(words_dict.values())
    words_dict = dict(sorted(words_dict.items(), key=lambda x: (x[0] if sum_of_all_dict_values % 2 == 0 else -x[1])))

    return linesep.join((f"{k} - {v}" for k, v in words_dict.items()))


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print("--------------------------")
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print("--------------------------")
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
