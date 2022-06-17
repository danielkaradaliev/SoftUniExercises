text = input()
char_dict = dict()

for char in text:
    if not char_dict.get(char):
        char_dict[char] = 0
    char_dict[char] += 1

sorted_keys = sorted(char_dict.keys())

for key in sorted_keys:
    print(f"{key}: {char_dict[key]} time/s")
