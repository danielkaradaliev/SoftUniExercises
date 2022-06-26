from collections import deque


def add_main_color(main_color):
    colors_found.append(main_color)

    for secondary_color in secondary_colors_found:
        add_secondary_color(secondary_color)


def add_secondary_color(secondary_color):
    if (secondary_color == "orange" and ("red" in colors_found and "yellow" in colors_found)) or \
            (secondary_color == "purple" and ("red" in colors_found and "blue" in colors_found)) or \
            (secondary_color == "green" and ("yellow" in colors_found and "blue" in colors_found)) and \
            secondary_color not in colors_found:
        colors_found.insert(secondary_colors_found[secondary_color], secondary_color)


strings = deque(input().split())

main_colors_to_find = {"red", "yellow", "blue"}
secondary_colors_to_find = {"orange", "purple", "green"}
colors_found = []
secondary_colors_found = {}

while strings:
    substrings_to_check = []
    first_substring = strings.popleft()
    second_substring = strings.pop() if strings else ""
    substrings = [first_substring, second_substring]

    substrings_to_check.append(first_substring + second_substring)
    substrings_to_check.append(second_substring + first_substring)

    for substring in substrings_to_check:
        if substring in main_colors_to_find:
            add_main_color(substring)
            break
        elif substring in secondary_colors_to_find:
            secondary_color_index = len(colors_found)
            secondary_colors_found[substring] = secondary_color_index
            add_secondary_color(substring)
            break
    else:
        index = len(strings) // 2
        for x in substrings[::-1]:
            substring_to_insert = x[:-1]
            if len(substring_to_insert):
                strings.insert(index, substring_to_insert)

print(colors_found)
