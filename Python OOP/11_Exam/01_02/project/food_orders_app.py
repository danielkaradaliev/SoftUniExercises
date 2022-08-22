from os import linesep

from project.client import Client
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu = list()
        self.clients_list = list()
        self.__next_order_id = 0

    def register_client(self, client_phone_number: str):
        if self.__get_client_by_phone_number(client_phone_number) is not None:
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {new_client.phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if self.__valid_meal_type(meal):
                self.menu.append(meal)

    def show_menu(self):
        self.__get_menu_not_ready_exception()
        return linesep.join([meal.details() for meal in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__get_menu_not_ready_exception()
        client = self.__get_client_by_phone_number(client_phone_number)
        if client is None:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals_to_add_to_shopping_cart = dict()

        for meal_name, quantity in meal_names_and_quantities.items():
            current_meal = self.__get_meal_by_name(meal_name)
            # Check if valid meal type???
            if current_meal is None:
                raise Exception(f"{meal_name} is not on the menu!")
            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {current_meal.get_type()}: {meal_name}!")
            meals_to_add_to_shopping_cart[meal_name] = quantity

        # Add meals to shopping cart
        for meal_name, quantity in meals_to_add_to_shopping_cart.items():
            current_meal = self.__get_meal_by_name(meal_name)
            meal_to_add_to_cart = None
            if current_meal.get_type() == "Dessert":
                meal_to_add_to_cart = Dessert(meal_name, current_meal.price, quantity)
            elif current_meal.get_type() == "Main Dish":
                meal_to_add_to_cart = MainDish(meal_name, current_meal.price, quantity)
            elif current_meal.get_type() == "Starter":
                meal_to_add_to_cart = Starter(meal_name, current_meal.price, quantity)

            current_meal.quantity -= quantity
            client.shopping_cart.append(meal_to_add_to_cart)

        return f"Client {client.phone_number} successfully ordered " \
               f"{', '.join([meal.name for meal in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        # You will always be given an existing client phone number.
        client = self.__get_client_by_phone_number(client_phone_number)
        self.__get_no_ordered_meals_exception(client)

        # Update menu quantities
        for meal in client.shopping_cart:
            menu_meal = self.__get_meal_by_name(meal.name)
            menu_meal.quantity += meal.quantity

        client.shopping_cart = list()
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__get_client_by_phone_number(client_phone_number)
        self.__get_no_ordered_meals_exception(client)
        new_order_id = self.__get_order_id()
        bill_to_pay = client.bill
        client.shopping_cart = list()
        return f"Receipt #{new_order_id} with total amount of {bill_to_pay:.2f} " \
               f"was successfully paid for {client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __get_client_by_phone_number(self, phone_number: str):
        for each_client in self.clients_list:
            if each_client.phone_number == phone_number:
                return each_client
        return None

    def __get_meal_by_name(self, meal_name):
        for each_meal in self.menu:
            if each_meal.name == meal_name:
                return each_meal
        return None

    def __get_menu_not_ready_exception(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    @staticmethod
    def __get_no_ordered_meals_exception(client):
        if not len(client.shopping_cart):
            raise "There are no ordered meals!"

    def __get_order_id(self):
        self.__next_order_id += 1
        return self.__next_order_id

    @staticmethod
    def __valid_meal_type(meal):
        return isinstance(meal, Meal) and meal.get_type() in ("Starter", "Main Dish", "Dessert")
