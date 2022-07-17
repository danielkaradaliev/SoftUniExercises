from project.animals.animal import Bird


class Owl(Bird):
    @property
    def types_of_food_eaten(self):
        return "Meat",

    @property
    def weight_gain(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def types_of_food_eaten(self):
        return "Vegetable", "Fruit", "Meat", "Seed"

    @property
    def weight_gain(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"
