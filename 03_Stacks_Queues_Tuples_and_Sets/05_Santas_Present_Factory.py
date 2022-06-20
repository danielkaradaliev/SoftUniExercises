from collections import deque

presents_dict = {
    "Bicycle": 0,
    "Doll": 0,
    "Teddy bear": 0,
    "Wooden train": 0
}

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])
christmas_successful = False

while materials and magic:
    if materials[-1] == 0:
        materials.pop()
        continue
    if magic[0] == 0:
        magic.popleft()
        continue

    current_materials = materials.pop()
    current_magic = magic.popleft()
    product = current_materials * current_magic

    if product < 0:
        s = current_materials + current_magic
        materials.append(s)
    elif product == 150:
        presents_dict["Doll"] += 1
    elif product == 250:
        presents_dict["Wooden train"] += 1
    elif product == 300:
        presents_dict["Teddy bear"] += 1
    elif product == 400:
        presents_dict["Bicycle"] += 1
    else:
        materials.append(current_materials + 15)

if (presents_dict["Doll"] > 0 and presents_dict["Wooden train"] > 0) or \
   (presents_dict["Teddy bear"] > 0 and presents_dict["Bicycle"] > 0):
    christmas_successful = True
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials.reverse()
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for toy, amount in {k: v for k, v in presents_dict.items() if v > 0}.items():
    print(f"{toy}: {amount}")
