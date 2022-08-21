class Validators:
    @staticmethod
    def validate_name(value: str, min_length: int, error_message: str):
        if value.isspace() or len(value) < min_length:
            raise ValueError(error_message)

    @staticmethod
    def validate_min_age(age: int, min_age: int, error_message: str):
        if age < min_age:
            raise ValueError(error_message)

    @staticmethod
    def validate_horse_max_speed(speed: int, max_speed: int, error_message: str):
        if speed > max_speed:
            raise ValueError(error_message)

    @staticmethod
    def validate_race_type(race_type: str, error_message: str):
        valid_race_types = ("Winter", "Spring", "Autumn", "Summer")
        if race_type not in valid_race_types:
            raise ValueError(error_message)
