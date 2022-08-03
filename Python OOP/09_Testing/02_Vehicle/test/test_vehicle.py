from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    FUEL = 75.0
    FUEL_CAPACITY = FUEL
    HORSE_POWER = 135
    FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.new_vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init__pass_correct_values__create_correct_instance(self):
        self.assertEqual(self.new_vehicle.fuel, self.FUEL)
        self.assertEqual(self.new_vehicle.capacity, self.FUEL_CAPACITY)
        self.assertEqual(self.new_vehicle.horse_power, self.HORSE_POWER)
        self.assertEqual(self.new_vehicle.fuel_consumption, self.FUEL_CONSUMPTION)

    def test__drive__valid_distance__expect_to_have_correct_fuel_remaining(self):
        distance_to_drive = 10
        self.new_vehicle.drive(distance_to_drive)
        self.assertEqual(self.new_vehicle.fuel, 62.5)

    def test__drive__valid_distance__expect_to_reach_destination_with_empty_tank(self):
        distance_to_drive = 60
        self.new_vehicle.drive(distance_to_drive)
        self.assertEqual(self.new_vehicle.fuel, 0)

    def test__drive__too_far__expect_to_raise(self):
        distance_to_drive = 100
        fuel_available = self.new_vehicle.fuel
        with self.assertRaises(Exception) as ex:
            self.new_vehicle.drive(distance_to_drive)
        self.assertEqual(str(ex.exception), "Not enough fuel")
        self.assertEqual(self.new_vehicle.fuel, fuel_available)

    def test__refuel__pass_valid_amount__expect_to_have_correct_amount_of_fuel_remaining(self):
        fuel_to_refuel = 17.5
        distance_to_drive = 50
        self.new_vehicle.drive(distance_to_drive)
        self.new_vehicle.refuel(fuel_to_refuel)
        self.assertEqual(self.new_vehicle.fuel, 30)

    def test__refuel_pass_invalid_amount__expect_to_raise(self):
        fuel_to_refuel = 60
        fuel_available = self.new_vehicle.fuel
        with self.assertRaises(Exception) as ex:
            self.new_vehicle.refuel(fuel_to_refuel)
        self.assertEqual(str(ex.exception), "Too much fuel")
        self.assertEqual(self.new_vehicle.fuel, fuel_available)

    def test__str__expect_correct_string(self):
        result = str(self.new_vehicle)
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
                          f"horse power with {self.FUEL} fuel left and {self.FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
