from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @staticmethod
    def get_type():
        return "Appaloosa"

    @staticmethod
    def max_speed():
        return 120

    @staticmethod
    def train_speed_increment():
        return 2
