from project.product import Product
from project.drink import Drink
from project.food import Food


class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.products.append(product)
        return None

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break
        return None

    def __repr__(self):
        linesep = "\n"
        return linesep.join([f"{product.name}: {product.quantity}" for product in self.products])
