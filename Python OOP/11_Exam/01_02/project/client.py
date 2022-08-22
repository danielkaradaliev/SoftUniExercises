from os import linesep


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = list()

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not (value and isinstance(value, str) and value[0] == "0" and len(value) == 10 and value.isdigit()):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

    @property
    def bill(self):
        return float(sum(meal.price * meal.quantity for meal in self.shopping_cart))

    def __str__(self):
        return f"Phone number: {self.phone_number}{linesep}" \
               f"Shopping cart: {self.shopping_cart}{linesep}" \
               f"Bill: {self.bill}"
