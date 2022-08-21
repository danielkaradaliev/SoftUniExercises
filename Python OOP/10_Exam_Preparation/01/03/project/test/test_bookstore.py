from unittest import TestCase, main

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def test__init__pass_valid_limit__expect_proper_object(self):
        bookstore_limit = 4
        new_bookstore = Bookstore(bookstore_limit)

        self.assertEqual(new_bookstore.books_limit, bookstore_limit)
        self.assertDictEqual(new_bookstore.availability_in_store_by_book_titles, dict())
        self.assertEqual(new_bookstore.books_limit, bookstore_limit)

    def test__init__pass_invalid_limit__expect_to_throw(self):
        bookstore_limit = -7

        with self.assertRaises(Exception) as ex:
            new_bookstore = Bookstore(bookstore_limit)
        self.assertEqual(str(ex.exception), f"Books limit of {bookstore_limit} is not valid")

    def test__books_limit_setter__pass_valid_value__expect_to_update(self):
        bookstore_limit = 5
        new_bookstore_limit = 8
        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.books_limit = new_bookstore_limit
        self.assertEqual(new_bookstore.books_limit, new_bookstore_limit)


    def test__len__expect_to_return_proper_number_of_books(self):
        bookstore_limit = 10
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore

        self.assertEqual(len(new_bookstore), 5)

    def test__receive_book__pass_more_books_than_capacity__expect_to_throw(self):
        bookstore_limit = 7
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        new_book = "Some very, very famous book"
        new_book_quantity = 6

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore

        with self.assertRaises(Exception) as ex:
            result = new_bookstore.receive_book(new_book, new_book_quantity)
        self.assertEqual(str(ex.exception), "Books limit is reached. Cannot receive more books!")
        self.assertDictEqual(new_bookstore.availability_in_store_by_book_titles, books_to_add_to_bookstore)

    def test__receive_book__pass_new_books_less_than_capacity__expect_to_add_them_and_return_proper_message(self):
        bookstore_limit = 10
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        new_book = "Some very, very famous book"
        new_book_quantity = 2
        expected_books = {
            "Some famous book": 3,
            "Some not so famous book": 2,
            "Some very, very famous book": 2
        }

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore
        result = new_bookstore.receive_book(new_book, new_book_quantity)

        self.assertDictEqual(new_bookstore.availability_in_store_by_book_titles, expected_books)
        self.assertEqual(result, f"{new_book_quantity} copies of {new_book} are available in the bookstore.")

    def test__receive_book__pass_existing_books_less_than_capacity__expect_to_add_them_and_return_proper_message(self):
        bookstore_limit = 10
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        new_book = "Some not so famous book"
        new_book_quantity = 2
        expected_books = {
            "Some famous book": 3,
            "Some not so famous book": 4,
        }
        expected_new_number_of_books = 4

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore
        result = new_bookstore.receive_book(new_book, new_book_quantity)

        self.assertDictEqual(new_bookstore.availability_in_store_by_book_titles, expected_books)
        self.assertEqual(result, f"{expected_new_number_of_books} copies of {new_book} are available in the bookstore.")

    def test__sell_book__pass_unavailable_book__expect_to_throw(self):
        bookstore_limit = 5
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        book_to_sell = "Some very disturbing book"
        copies_to_cell = 5

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore

        with self.assertRaises(Exception) as ex:
            result = new_bookstore.sell_book(book_to_sell, copies_to_cell)

        self.assertEqual(str(ex.exception), f"Book {book_to_sell} doesn't exist!")

    def test__sell_book__pass_available_book_with_incorrect_amount__expect_to_fail(self):
        bookstore_limit = 5
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        book_to_sell = "Some not so famous book"
        copies_to_cell = 5
        expected_books_left = books_to_add_to_bookstore[book_to_sell]

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore

        with self.assertRaises(Exception) as ex:
            result = new_bookstore.sell_book(book_to_sell, copies_to_cell)

        self.assertEqual(str(ex.exception), f"{book_to_sell} has not enough copies to sell. Left: {expected_books_left}")

    def test__sell_book__pass_available_book_with_correct_amount__expect_to_sell_and_return_proper_message(self):
        bookstore_limit = 5
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        book_to_sell = "Some not so famous book"
        copies_to_cell = 2
        expected_remainder = books_to_add_to_bookstore[book_to_sell] - copies_to_cell

        new_bookstore = Bookstore(bookstore_limit)
        expected_books_sold = new_bookstore.total_sold_books + copies_to_cell
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore
        result = new_bookstore.sell_book(book_to_sell, copies_to_cell)

        self.assertEqual(new_bookstore.availability_in_store_by_book_titles[book_to_sell], expected_remainder)
        self.assertEqual(new_bookstore.total_sold_books, expected_books_sold)
        self.assertEqual(result, f"Sold {copies_to_cell} copies of {book_to_sell}")

    def test__str__expect_proper_string(self):
        bookstore_limit = 5
        books_to_add_to_bookstore = {
            "Some famous book": 3,
            "Some not so famous book": 2
        }
        book_to_sell = "Some not so famous book"
        copies_to_cell = 1
        expected_remainder = books_to_add_to_bookstore[book_to_sell] - copies_to_cell
        expected_sold_books = copies_to_cell

        new_bookstore = Bookstore(bookstore_limit)
        new_bookstore.availability_in_store_by_book_titles = books_to_add_to_bookstore
        result = new_bookstore.sell_book(book_to_sell, copies_to_cell)

        expected_result = f"Total sold books: {expected_sold_books}" \
                          f"Current availability: {expected_remainder}" \
                          f" - Some famous book: 3 copies" \
                          f" - Some not so famous book: 1 copies"


if __name__ == "__main__":
    main()
