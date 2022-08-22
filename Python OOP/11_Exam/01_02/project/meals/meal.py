from abc import ABC, abstractmethod


class Meal(ABC):
    @abstractmethod
    def __init__(self, name: str, price: float, quantity=None):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price!")
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value if value is not None else self.default_quantity

    @staticmethod
    @abstractmethod
    def get_type():
        return "Meal"

    @property
    @abstractmethod
    def default_quantity(self):
        return 0

    def details(self):
        return f"{self.get_type()} {self.name}: {self.price:.2f}lv/piece"
