from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    SHOP_NAME = "SuperShop"
    BUDGET = 50

    def setUp(self) -> None:

        self.new_shopping_cart = ShoppingCart(self.SHOP_NAME, self.BUDGET)

    def test__init__pass_valid_parameters__expect_proper_object(self):
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, dict())

    def test__init__pass_invalid_shop_names__expect_to_throw(self):
        lowercase_name = "too_small_to_roll"
        with self.assertRaises(ValueError) as ex:
            _ = ShoppingCart(lowercase_name, self.BUDGET)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

        name_contains_numbers = "Office 1 Superstore"
        with self.assertRaises(ValueError) as ex:
            _ = ShoppingCart(name_contains_numbers, self.BUDGET)
        self.assertEqual(str(ex.exception), "Shop must contain only letters and must start with capital letter!")

    def test__add_to_cart__pass_valid_product_and_price__expect_to_add_to_cart(self):
        product_name = "pen"
        product_price = 1.25
        result_1 = self.new_shopping_cart.add_to_cart(product_name, product_price)
        another_product_name = "pencil"
        another_product_price = 0.75
        result_2 = self.new_shopping_cart.add_to_cart(another_product_name, another_product_price)
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, {
            "pen": 1.25,
            "pencil": 0.75
        })
        self.assertEqual(result_1, f"{product_name} product was successfully added to the cart!")
        self.assertEqual(result_2, f"{another_product_name} product was successfully added to the cart!")

    def test__add_to_cart__pass_too_expensive_product__expect_to_throw(self):
        product_name = "paper"
        product_price = 9.99
        result_1 = self.new_shopping_cart.add_to_cart(product_name, product_price)
        another_product_name = "printer"
        another_product_price = 299.99
        with self.assertRaises(ValueError) as ex:
            _ = self.new_shopping_cart.add_to_cart(another_product_name, another_product_price)
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, {
            "paper": 9.99
        })
        self.assertEqual(result_1, f"{product_name} product was successfully added to the cart!")
        self.assertEqual(str(ex.exception), f"Product {another_product_name} cost too much!")

    def test__remove_from_cart__pass_existing_product__expect_to_remove_from_cart(self):
        product_name = "scissors"
        product_price = 5.19
        result_1 = self.new_shopping_cart.add_to_cart(product_name, product_price)
        another_product_name = "glue"
        another_product_price = 0.99
        result_2 = self.new_shopping_cart.add_to_cart(another_product_name, another_product_price)
        yet_another_product_name = "colored pen"
        yet_another_product_price = 2.29
        result_3 = self.new_shopping_cart.add_to_cart(yet_another_product_name, yet_another_product_price)
        result_4 = self.new_shopping_cart.remove_from_cart(another_product_name)
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, {
            "scissors": 5.19,
            "colored pen": 2.29
        })
        self.assertEqual(result_4, f"Product {another_product_name} was successfully removed from the cart!")

    def test__remove_from_cart__pass_invalid_product__expect_to_throw(self):
        product_name = "lamp"
        product_price = 25.99
        result_1 = self.new_shopping_cart.add_to_cart(product_name, product_price)
        another_product_name = "bulb"
        another_product_price = 3.99
        result_2 = self.new_shopping_cart.add_to_cart(another_product_name, another_product_price)
        invalid_product_name = "colored pen"
        invalid_product_price = 2.29
        with self.assertRaises(ValueError) as ex:
            _ = self.new_shopping_cart.remove_from_cart(invalid_product_name)
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, {
            "lamp": 25.99,
            "bulb": 3.99
        })
        self.assertEqual(str(ex.exception), f"No product with name {invalid_product_name} in the cart!")

    def test__add__sum_two_shopping_carts__expect_proper_object(self):
        another_shop_name = "Top"
        another_shop_budget = 80
        self_shopping_cart = {
            "water": 0.99,
            "beer": 1.99,
            "milk": 2.19
        }
        self.new_shopping_cart.products = self_shopping_cart
        another_shopping_cart_products = {
            "beer": 1.49,
            "juice": 3.39
        }
        another_shopping_cart = ShoppingCart(another_shop_name, another_shop_budget)
        another_shopping_cart.products = another_shopping_cart_products
        expected_shop_name = f"{self.SHOP_NAME}{another_shop_name}"
        expected_budget = self.BUDGET + another_shop_budget
        expected_shopping_cart_products = {
            "water": 0.99,
            "beer": 1.49,
            "milk": 2.19,
            "juice": 3.39
        }

        result_shopping_cart = self.new_shopping_cart + another_shopping_cart
        self.assertEqual(result_shopping_cart.shop_name, expected_shop_name)
        self.assertEqual(result_shopping_cart.budget, expected_budget)
        self.assertDictEqual(result_shopping_cart.products, expected_shopping_cart_products)

    def test__buy_products__total_sum_less_than_budget__expect_to_buy(self):
        self_shopping_cart = {
            "ham": 19.99,
            "bacon": 15.99,
            "mushrooms": 2.19
        }
        self.new_shopping_cart.products = self_shopping_cart
        expected_total_sum = sum(self_shopping_cart.values())
        result = self.new_shopping_cart.buy_products()
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, self_shopping_cart)
        self.assertEqual(result, f"Products were successfully bought! Total cost: {expected_total_sum:.2f}lv.")

    def test__buy_products__total_sum_over_budget__expect_to_throw(self):
        self_shopping_cart = {
            "umbrella": 29.99,
            "raincoat": 89.99
        }
        self.new_shopping_cart.products = self_shopping_cart
        expected_over_budget = sum(self_shopping_cart.values()) - self.BUDGET
        with self.assertRaises(ValueError) as ex:
            _ = self.new_shopping_cart.buy_products()
        self.assertEqual(self.new_shopping_cart.shop_name, self.SHOP_NAME)
        self.assertEqual(self.new_shopping_cart.budget, self.BUDGET)
        self.assertDictEqual(self.new_shopping_cart.products, self_shopping_cart)
        self.assertEqual(str(ex.exception), f"Not enough money to buy the products! Over budget with {expected_over_budget:.2f}lv!")


if __name__ == "__main__":
    main()
