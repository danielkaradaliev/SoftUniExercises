class Vet:
    animals = list()
    space = 5

    def __init__(self, name: str, animals: list = None):
        self.name = name
        self.animals = animals if animals is not None else list()
        Vet.animals += self.animals
        Vet.space = 5 - len(Vet.animals)

    def register_animal(self, animal_name: str):
        if Vet.space <= 0:
            return "Not enough space"
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        Vet.space -= 1
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name: str):
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"
        Vet.animals.remove(animal_name)
        Vet.space += 1
        if animal_name in self.animals:
            self.animals.remove(animal_name)
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
