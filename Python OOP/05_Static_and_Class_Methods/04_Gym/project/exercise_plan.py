class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = ExercisePlan.get_next_id()

    @staticmethod
    def get_next_id():
        new_id = ExercisePlan.id
        ExercisePlan.id += 1
        return new_id

    @staticmethod
    def from_hours(trainer_id: int, equipment_id: int, hours: int):
        minutes = hours * 60
        return ExercisePlan(trainer_id, equipment_id, minutes)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
