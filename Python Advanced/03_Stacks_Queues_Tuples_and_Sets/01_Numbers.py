first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
sets_dict = {
    "First": first_set,
    "Second": second_set
}
number = int(input())

for _ in range(number):
    command = input().split()
    if command[0] == "Add":
        sets_dict[command[1]] = sets_dict[command[1]].union([int(x) for x in command[2:]])
    elif command[0] == "Remove":
        sets_dict[command[1]] = sets_dict[command[1]].difference([int(x) for x in command[2:]])
    elif command[0] == "Check":
        if sets_dict["First"].issubset(sets_dict["Second"]) or sets_dict["Second"].issubset(sets_dict["First"]):
            print("True")
        else:
            print("False")

print(", ".join(sorted([str(x) for x in sets_dict["First"]])))
print(", ".join(sorted([str(x) for x in sets_dict["Second"]])))
