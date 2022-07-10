class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        linesep = "\n"
        return f"Player: {self.__name}{linesep}" \
               f"Sprint: {self.__sprint}{linesep}" \
               f"Dribble: {self.__dribble}{linesep}" \
               f"Passing: {self.__passing}{linesep}" \
               f"Shooting: {self.__shooting}"
