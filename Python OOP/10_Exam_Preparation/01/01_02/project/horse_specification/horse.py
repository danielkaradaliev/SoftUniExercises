from abc import ABC, abstractmethod

from project.validators.validators import Validators


class Horse(ABC):
    @abstractmethod
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.__is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validators.validate_name(value, self.__name_min_length, self.__get_name_invalid_error_message(value))
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validators.validate_horse_max_speed(value, self.max_speed(), self.__get_speed_error_message())
        self.__speed = value

    @property
    def is_taken(self):
        return self.__is_taken

    @staticmethod
    @abstractmethod
    def get_type():
        pass

    @property
    def __name_min_length(self):
        return 4

    @staticmethod
    def __get_name_invalid_error_message(name):
        return f"Horse name {name} is less than 4 symbols!"

    @staticmethod
    @abstractmethod
    def max_speed():
        pass

    @staticmethod
    def __get_speed_error_message():
        return "Horse speed is too high!"

    @staticmethod
    @abstractmethod
    def train_speed_increment():
        pass

    def train(self):
        new_speed = self.speed + self.train_speed_increment
        if new_speed > self.max_speed:
            new_speed = self.max_speed
        self.speed = new_speed
