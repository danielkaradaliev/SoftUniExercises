class User:
    def __init__(self, user_id: int, username: str):
        self.id = user_id
        self.username = username
        self.books = list()

    def info(self):
        return ", ".join(self.books)

    def __str__(self):
        return f"{self.id}, {self.username}, {self.books}"
