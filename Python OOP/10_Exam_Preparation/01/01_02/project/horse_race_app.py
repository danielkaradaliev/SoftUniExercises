from project.horse_race import HorseRace
from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    def __init__(self):
        self.horses = list()
        self.jockeys = list()
        self.horse_races = list()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        """
        The method creates a horse and adds it to the horses' list.
            - If the horse is successfully created and added,
              the method should return the message: "{horse_type} horse {horse_name} is added."
            - If a horse with the same name already exists,
              raise an Exception with the message "Horse {horse_name} has been already added!"
            - The valid types of horse breeds are "Appaloosa" and "Thoroughbred". All other types must be ignored.
        """

        if horse_type not in ("Appaloosa", "Thoroughbred"):
            return None

        if self.__get_horse_by_name(horse_name) is not None:
            self.__get_horse_name_not_unique_exception(horse_name)

        # TODO: Factory???
        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        """
        The method creates a jockey and adds it to the jockeys' list.
            - If the jockey is successfully created and added,
              the method should return the message "Jockey {jockey_name} is added."
            - If a jockey with the given name already exists,
              raise an Exception with the message "Jockey {jockey_name} has been already added!"
        """

        if self.__get_jockey_by_name(jockey_name) is not None:
            self.__get_jockey_name_not_unique_exception(jockey_name)

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        """
        The method creates a race and adds it to the horse races' list.
            - When it is successfully created and added,
              the method returns the message "Race {race_type} is created."
            - A race of each of the 4 types can be created just once. 
              If a race of the same type already exists,
              raise an Exception with the message "Race {race type} has been already created!"
        """
        if self.__get_race_by_name(race_type) is not None:
            self.__get_race_already_added_exception(race_type)

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        """
        Sets the last horse added from the given horse type to the jockey with the given name (if they both exist).
            - If the jockey does NOT exist in the jockeys' list,
              raise an Exception with the message "Jockey {jockey_name} could not be found!"
            - If there is no available horse (all horses of that type are taken,
              or no horse of that type exists) of the given type in the horses' list,
              raise an Exception with the message "Horse breed {horse_type} could not be found!".
            - If there is an available horse (the horse is not taken), but the jockey already has a horse,
              return the message: "Jockey {jockey_name} already has a horse."
            - If the horse can be added to the jockey, take it, and set it to the jockey.
              Then, return the message: "Jockey {jockey_name} will ride the horse {horse_name}."
        """

        jockey = self.__get_jockey_by_name(jockey_name)
        horse = self.__get_free_horse_by_type(horse_type)

        if jockey is None:
            self.__get_jockey_not_found_exception(jockey_name)

        if horse is None:
            self.__get_free_horse_not_found_exception(horse_type)

        if jockey.horse is not None:
            return self.__get_jockey_already_has_a_horse_message(jockey_name)

        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        """
        Adds a jockey (object) to the given horse race type (if they both exist).
        A jockey can only participate in a horse race if he has a horse.
            - If a horse race of that type does NOT exist in the list with horse races,
              raise an Exception with the message "Race {race_type} could not be found!"
            - If the jockey does NOT exist in the jockeys' list,
              raise an Exception with the message "Jockey {jockey_name} could not be found!"
            - If the jockey is on the jockeys' list, but he/she doesn't have a horse,
              raise an Exception with the message "Jockey {jockey_name} cannot race without a horse!"
            - If the jockey has already been added to the horse race,
              return the message "Jockey {jockey_name} has been already added to the {race_type} race."
            - If both the race type and the jockey exist and the jockey has a horse,
              add the jockey (object) to the given horse race and return the message:
              "Jockey {jockey_name} added to the {race_type} race."
        """
        jockey = self.__get_jockey_by_name(jockey_name)
        race = self.__get_race_by_name(race_type)

        if race is None:
            self.__get_race_not_found_exception(race_type)

        if jockey is None:
            self.__get_jockey_not_found_exception(jockey_name)

        if jockey.horse is None:
            self.__get_jockey_has_no_horse_exception(jockey_name)

        if jockey in race.jockeys:
            return self.__get_jockey_already_joined_the_race_message(jockey_name, race_type)

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        """
        Race commences!
            - If the horse race does NOT exist,
              raise an Exception with the message "Race {race_type} could not be found!"
            - The participants in a horse race must be at least 2.
              Otherwise, raise an Exception with the message "Horse race {race_type} needs at least two participants!"
            - If the race can be started, you should choose the winner -
              he/she is the jockey who rode the horse with the highest speed.
              Note: there will NOT be two or more jockeys riding their horse at the same highest speed.
              In the end, return the message:
              "The winner of the {race_type} race, with a speed of {highest_speed}km/h is {jockey_name}!
              Winner's horse: {horse_name}."
        """

        race = self.__get_race_by_name(race_type)

        if race is None:
            self.__get_race_not_found_exception(race_type)

        if len(race.jockeys) < 2:
            self.__get_too_few_participants_exception(race_type)

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}!" \
               f" Winner's horse: {winner.horse.name}."

    def __get_horse_by_name(self, horse_name: str):
        for each_horse in self.horses:
            if each_horse.name == horse_name:
                return each_horse
        return None

    def __get_free_horse_by_type(self, horse_type: str):
        for each_horse in [horse for horse in self.horses if horse.get_type() == horse_type and not horse.is_taken]:
            return each_horse
        return None

    def __get_jockey_by_name(self, jockey_name: str):
        for each_jockey in self.jockeys:
            if each_jockey.name == jockey_name:
                return each_jockey
        return None

    def __get_race_by_name(self, race_name: str):
        for each_race in self.horse_races:
            if each_race.race_type == race_name:
                return each_race
        return None

    @staticmethod
    def __get_horse_name_not_unique_exception(horse_name: str):
        raise Exception ("Horse {horse_name} has been already added!")

    @staticmethod
    def __get_jockey_name_not_unique_exception(jockey_name: str):
        raise Exception(f"Jockey {jockey_name} has been already added!")

    @staticmethod
    def __get_race_already_added_exception(race_type: str):
        raise Exception(f"Race {race_type} has been already created!")

    @staticmethod
    def __get_jockey_not_found_exception(jockey_name: str):
        raise Exception(f"Jockey {jockey_name} could not be found!")

    @staticmethod
    def __get_free_horse_not_found_exception(horse_type: str):
        raise Exception(f"Horse breed {horse_type} could not be found!")

    @staticmethod
    def __get_race_not_found_exception(race_type: str):
        raise Exception(f"Race {race_type} could not be found!")

    @staticmethod
    def __get_jockey_has_no_horse_exception(jockey_name: str):
        raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

    @staticmethod
    def __get_too_few_participants_exception(race_type: str):
        raise Exception(f"Horse race {race_type} needs at least two participants!")

    @staticmethod
    def __get_jockey_already_has_a_horse_message(jockey_name: str):
        return f"Jockey {jockey_name} already has a horse."

    @staticmethod
    def __get_jockey_already_joined_the_race_message(jockey_name: str, race_type: str):
        return f"Jockey {jockey_name} has been already added to the {race_type} race."
