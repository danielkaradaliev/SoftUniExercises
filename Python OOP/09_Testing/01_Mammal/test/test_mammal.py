from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    NAME = "Pesho"
    TYPE = "Gligan"
    SOUND = "Gruh-gruh"

    def setUp(self):
        self.new_mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.new_mammal.name)
        self.assertEqual(self.TYPE, self.new_mammal.type)
        self.assertEqual(self.SOUND, self.new_mammal.sound)

    def test__get_kingdom__expect_to_be_animal(self):
        self.assertEqual(self.new_mammal.get_kingdom(), "animals")

    def test__make_sound__expect_correct_sound(self):
        self.assertEqual(self.new_mammal.make_sound(), f"{self.NAME} makes {self.SOUND}")

    def test__info__expect_correct_info(self):
        self.assertEqual(self.new_mammal.info(), f"{self.NAME} is of type {self.TYPE}")


if __name__ == "__main__":
    main()
