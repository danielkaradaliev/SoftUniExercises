from project.meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name: str, price: float, quantity=None):
        super().__init__(name, price, quantity)

    @staticmethod
    def get_type():
        return "Dessert"

    @property
    def default_quantity(self):
        return 30
