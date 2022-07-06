class Registration:
    @staticmethod
    def add_user(user, library):
        if user.id in [x.id for x in library.user_records]:
            return f"User with id = {user.id} already registered in the library!"
        library.user_records.append(user)
        return None

    @staticmethod
    def remove_user(user, library):
        for index, each_user in enumerate(library.user_records):
            if each_user.id == user.id:
                library.user_records.pop(index)
                return None
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id: int, new_username: str, library):
        for user in library.user_records:
            if user.id == user_id:
                if user.username == new_username:
                    return "Please check again the provided username - " \
                           "it should be different than the username used so far!"
                if user.username in library.rented_books.keys():
                    # Performance concern? Want to preserve the key order though...
                    library.rented_books = {username if username != new_username else new_username: books
                                            for username, books in library.rented_books.items()}
                user.username = new_username
                return f"Username successfully changed to: {user.username} for user id: {user.id}"
        else:
            return f"There is no user with id = {user_id}!"
