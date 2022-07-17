from project.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def types_of_food_eaten(self):
        return "Vegetable", "Fruit"

    @property
    def weight_gain(self):
        return 0.1

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):
    @property
    def types_of_food_eaten(self):
        return "Meat",

    @property
    def weight_gain(self):
        return 0.4

    @staticmethod
    def make_sound():
        return "Woof!"


class Cat(Mammal):
    @property
    def types_of_food_eaten(self):
        return "Vegetable", "Meat",

    @property
    def weight_gain(self):
        return 0.3

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):
    @property
    def types_of_food_eaten(self):
        return "Vegetable", "Meat",

    @property
    def weight_gain(self):
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
