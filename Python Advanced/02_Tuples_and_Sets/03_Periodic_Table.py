lines = int(input())
chemical_compounds = set()

for _ in range(lines):
    for chemical_compound in input().split():
        chemical_compounds.add(chemical_compound)

for chemical_compound in chemical_compounds:
    print(chemical_compound)
