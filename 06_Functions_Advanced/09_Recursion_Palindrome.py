def palindrome(word, index):
    word_length = len(word)
    if index <= len(word) / 2:
        if word[index] == word[word_length - index - 1]:
            return palindrome(word, index + 1)
        else:
            return f"{word} is not a palindrome"
    else:
        return f"{word} is a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
