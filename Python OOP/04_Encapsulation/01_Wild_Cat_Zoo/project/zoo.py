from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal: Animal, price: int):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker_name == worker.name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        funds_needed = sum([worker.salary for worker in self.workers])
        if funds_needed > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= funds_needed
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        funds_needed = sum([animal.money_for_care for animal in self.animals])
        if funds_needed > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= funds_needed
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount
        return None

    def animals_status(self):
        linesep = "\n"
        lions = [x for x in self.animals if isinstance(x, Lion)]
        tigers = [x for x in self.animals if isinstance(x, Tiger)]
        cheetahs = [x for x in self.animals if isinstance(x, Cheetah)]
        total_animals_str = f"You have {len(self.animals)} animals" + linesep
        total_lions_str = f"----- {len(lions)} Lions:{linesep}" + \
                          f"{linesep}".join([str(x) for x in lions]) + linesep
        total_tigers_str = f"----- {len(tigers)} Tigers:{linesep}" + \
                           f"{linesep}".join([str(x) for x in tigers]) + linesep
        total_cheetahs_str = f"----- {len(cheetahs)} Cheetahs:{linesep}" + \
                             f"{linesep}".join([str(x) for x in cheetahs])
        return total_animals_str + total_lions_str + total_tigers_str + total_cheetahs_str

    def workers_status(self):
        linesep = "\n"
        keepers = [x for x in self.workers if isinstance(x, Keeper)]
        caretakers = [x for x in self.workers if isinstance(x, Caretaker)]
        vets = [x for x in self.workers if isinstance(x, Vet)]
        total_workers_str = f"You have {len(self.workers)} workers" + linesep
        total_keepers_str = f"----- {len(keepers)} Keepers:{linesep}" + \
                            f"{linesep}".join([str(x) for x in keepers]) + linesep
        total_caretakers_str = f"----- {len(caretakers)} Caretakers:{linesep}" + \
                               f"{linesep}".join([str(x) for x in caretakers]) + linesep
        total_vets_str = f"----- {len(vets)} Vets:{linesep}" + \
                               f"{linesep}".join([str(x) for x in vets])
        return total_workers_str + total_keepers_str + total_caretakers_str + total_vets_str
