from abc import ABC, abstractmethod


class Vehicle(ABC):
    SUMMER_CONSUMPTION_INCREASE = 0

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        fuel_required = distance * (self.fuel_consumption + self.SUMMER_CONSUMPTION_INCREASE)
        if self.fuel_quantity > fuel_required:
            self.fuel_quantity -= fuel_required

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    SUMMER_CONSUMPTION_INCREASE = 0.9

    def drive(self, distance: float):
        super().drive(distance)

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_CONSUMPTION_INCREASE = 1.6

    def drive(self, distance: float):
        super().drive(distance)

    def refuel(self, fuel: float):
        self.fuel_quantity += (fuel * 0.95)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
