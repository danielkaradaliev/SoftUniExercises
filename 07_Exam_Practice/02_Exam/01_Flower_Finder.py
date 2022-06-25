from collections import deque


def word_char_found(word):
    return tuple([[char, False] for char in word])


def print_vowels_and_consonants(vowels, consonants):
    if len(vowels):
        print(f"Vowels left: {' '.join((x for x in vowels))}")
    if len(consonants):
        print(f"Consonants left: {' '.join((x for x in consonants))}")
    return None


vowels = deque(input().split())
consonants = deque(input().split())

words_of_interest = ("rose", "tulip", "lotus", "daffodil")
word_dict = dict({word: word_char_found(word) for word in words_of_interest})
word_found = ""

while True:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word, char_map in word_dict.items():
        for char in char_map:
            if vowel == char[0]:
                char[1] = True
            if consonant == char[0]:
                char[1] = True

        if all((x[1] for x in char_map)):
            word_found = word
            break

    if word_found:
        print(f"Word found: {word_found}")
        print_vowels_and_consonants(vowels, consonants)
        break

    if not (len(vowels) and len(consonants)):
        print("Cannot find any word!")
        print_vowels_and_consonants(vowels, consonants)
        break
