class Library:
    def __init__(self):
        self.user_records = list()
        self.books_available = dict()
        self.rented_books = dict()

    def get_book(self, author: str, book_name: str, days_to_return: int, user):
        for index, each_book in enumerate(self.books_available[author]):
            if book_name == each_book:
                if not self.rented_books.get(user.username):
                    self.rented_books[user.username] = dict()
                self.rented_books[user.username][book_name] = days_to_return
                self.books_available[author].pop(index)
                user.books.append(book_name)
                return f"{book_name} successfully rented for the next {days_to_return} days!"

        for rented_books in self.rented_books.values():
            for rented_book, days_to_return_left in rented_books.items():
                if book_name == rented_book:
                    return f"The book \"{book_name}\" is already rented" \
                           f" and will be available in {days_to_return_left} days!"

        return None

    def return_book(self, author: str, book_name: str, user):
        for books in self.rented_books.values():
            for book in books.keys():
                if book == book_name:
                    self.books_available[author].append(book_name)
                    del(self.rented_books[user.username][book])
                    user.books.remove(book_name)
                    return None

        return f"{user.username} doesn't have this book in his/her records!"
