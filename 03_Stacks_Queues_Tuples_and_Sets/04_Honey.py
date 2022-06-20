from collections import deque

honey_made = 0
working_bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])

while working_bees and nectar:
    matched_bee = 0
    matched_nectar = 0

    while nectar:
        if nectar[-1] >= working_bees[0]:
            matched_bee = working_bees.popleft()
            matched_nectar = nectar.pop()
            break
        else:
            nectar.pop()

    if matched_nectar == 0:
        break

    symbol = symbols.popleft()
    if symbol == "+":
        honey_made += abs(matched_bee + matched_nectar)
    elif symbol == "-":
        honey_made += abs(matched_bee - matched_nectar)
    elif symbol == "*":
        honey_made += abs(matched_bee * matched_nectar)
    elif symbol == "/":
        honey_made += abs(matched_bee / matched_nectar)

print(f"Total honey made: {honey_made}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
