input_text = [x.strip().split() for x in input().split("|")][::-1]

flattened_list = [x for y in input_text for x in y]

print(f"{' '.join(flattened_list)}")
