from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def types_of_food_eaten(self):
        raise NotImplemented

    @property
    @abstractmethod
    def weight_gain(self):
        raise NotImplemented

    @staticmethod
    @abstractmethod
    def make_sound():
        raise NotImplemented

    @abstractmethod
    def __repr__(self):
        raise NotImplemented

    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.types_of_food_eaten:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.weight += (self.weight_gain * food.quantity)
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @staticmethod
    @abstractmethod
    def make_sound():
        raise NotImplemented

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    @staticmethod
    @abstractmethod
    def make_sound():
        raise NotImplemented

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
