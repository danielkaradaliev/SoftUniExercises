def age_assignment(*args, **kwargs):
    from os import linesep
    people = {}
    names = args
    for first_letter, age in kwargs.items():
        for name in names:
            if first_letter == name[0]:
                people[name] = age
                break

    sorted_names = dict(sorted(people.items(), key=lambda x: x[0]))
    return linesep.join((f"{k} is {v} years old." for k, v in sorted_names.items()))


print(age_assignment("Peter", "George", G=26, P=19))
print("----------------------------------")
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
