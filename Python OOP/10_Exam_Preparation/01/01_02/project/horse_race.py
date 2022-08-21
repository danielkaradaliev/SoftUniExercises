from project.validators.validators import Validators


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = list()

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validators.validate_race_type(value, self.__get_invalid_race_type_error_message())
        self.__race_type = value

    @staticmethod
    def __get_invalid_race_type_error_message():
        return "Race type does not exist!"
