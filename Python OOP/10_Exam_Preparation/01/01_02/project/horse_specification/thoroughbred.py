from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @staticmethod
    def get_type():
        return "Thoroughbred"

    @staticmethod
    def max_speed():
        return 140

    @staticmethod
    def train_speed_increment():
        return 3
