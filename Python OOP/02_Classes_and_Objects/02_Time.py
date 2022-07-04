class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        Time.validate_time(self, hours, minutes, seconds)

    def validate_time(self, set_hours: int, set_minutes: int, set_seconds: int):
        hours = set_hours
        minutes = set_minutes
        seconds = set_seconds

        if seconds > Time.max_seconds:
            increment_minutes = seconds // (Time.max_seconds + 1)
            minutes += increment_minutes
            seconds %= (Time.max_seconds + 1)
        if minutes > Time.max_minutes:
            increment_hours = minutes // (Time.max_minutes + 1)
            hours += increment_hours
            minutes %= (Time.max_minutes + 1)
        if hours > Time.max_hours:
            hours %= (Time.max_hours + 1)

        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        Time.validate_time(self, hours, minutes, seconds)

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        Time.validate_time(self, self.hours, self.minutes, self.seconds + 1)
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
