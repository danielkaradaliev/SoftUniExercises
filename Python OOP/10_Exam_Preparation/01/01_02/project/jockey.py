from project.validators.validators import Validators


class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validators.validate_name(value, self.__min_name_length, self.__get_invalid_name_error_message())
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validators.validate_min_age(value, self.__min_age, self.__get_invalid_age_error_message())
        self.__age = value

    @property
    def __min_name_length(self):
        return 1

    @staticmethod
    def __get_invalid_name_error_message():
        return "Name should contain at least one character!"

    @property
    def __min_age(self):
        return 18

    @staticmethod
    def __get_invalid_age_error_message():
        return "Jockeys must be at least 18 to participate in the race!"
