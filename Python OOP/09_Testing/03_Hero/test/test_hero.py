from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    MY_USERNAME = "Gincho"
    MY_LEVEL = 5
    MY_HEALTH = 150
    MY_DAMAGE = 4
    ENEMY_USERNAME = "Enemy"
    ENEMY_LEVEL = 3
    ENEMY_HEALTH = 100
    ENEMY_DAMAGE = 5

    def setUp(self) -> None:
        self.my_hero = Hero(self.MY_USERNAME, self.MY_LEVEL, self.MY_HEALTH, self.MY_DAMAGE)
        self.enemy_hero = Hero(self.ENEMY_USERNAME, self.ENEMY_LEVEL, self.ENEMY_HEALTH, self.ENEMY_DAMAGE)

    def test__init__expect_proper_object(self):
        self.assertEqual(self.my_hero.username, self.MY_USERNAME)
        self.assertEqual(self.my_hero.level, self.MY_LEVEL)
        self.assertEqual(self.my_hero.health, self.MY_HEALTH)
        self.assertEqual(self.my_hero.damage, self.MY_DAMAGE)

        self.assertEqual(self.enemy_hero.username, self.ENEMY_USERNAME)
        self.assertEqual(self.enemy_hero.level, self.ENEMY_LEVEL)
        self.assertEqual(self.enemy_hero.health, self.ENEMY_HEALTH)
        self.assertEqual(self.enemy_hero.damage, self.ENEMY_DAMAGE)

    def test__battle__fight_yourself__expect_to_raise(self):
        my_expected_level = self.my_hero.level
        my_expected_health = self.my_hero.health
        my_expected_damage = self.my_hero.damage

        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.my_hero)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")
        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

    def test__battle__have_less_than_0_health__expect_to_raise(self):
        my_expected_level = self.my_hero.level
        my_expected_health = 0
        my_expected_damage = self.my_hero.damage
        self.my_hero.health = my_expected_health

        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")
        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

    def test__battle__enemy_has_less_than_0_health__expect_to_raise(self):
        my_expected_level = self.my_hero.level
        my_expected_health = self.my_hero.health
        my_expected_damage = self.my_hero.damage

        enemy_expected_level = self.enemy_hero.level
        enemy_expected_health = 0
        enemy_expected_damage = self.enemy_hero.damage
        self.enemy_hero.health = enemy_expected_health

        with self.assertRaises(Exception) as ex:
            self.my_hero.battle(self.enemy_hero)
        self.assertEqual(str(ex.exception), f"You cannot fight {self.enemy_hero.username}. He needs to rest")
        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

        self.assertEqual(self.enemy_hero.level, enemy_expected_level)
        self.assertEqual(self.enemy_hero.health, enemy_expected_health)
        self.assertEqual(self.enemy_hero.damage, enemy_expected_damage)

    def test__battle__fight_enemy__expect_to_draw_and_have_unchanged_stats(self):
        my_expected_level = self.my_hero.level
        my_expected_damage = self.my_hero.damage
        my_damage_to_inflict = self.my_hero.level * self.my_hero.damage

        enemy_expected_level = self.enemy_hero.level
        enemy_expected_damage = self.enemy_hero.damage
        enemy_damage_to_inflict = self.enemy_hero.level * self.enemy_hero.damage

        # Set low health values
        self.my_hero.health = 10
        self.enemy_hero.health = 18

        my_expected_health = self.my_hero.health - enemy_damage_to_inflict
        enemy_expected_health = self.enemy_hero.health - my_damage_to_inflict

        battle_result = self.my_hero.battle(self.enemy_hero)
        expected_result = "Draw"

        self.assertEqual(battle_result, expected_result)

        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

        self.assertEqual(self.enemy_hero.level, enemy_expected_level)
        self.assertEqual(self.enemy_hero.health, enemy_expected_health)
        self.assertEqual(self.enemy_hero.damage, enemy_expected_damage)

    def test__battle__fight_enemy__expect_to_win_and_have_updated_stats(self):
        my_expected_level = self.my_hero.level + 1
        my_expected_damage = self.my_hero.damage + 5
        my_damage_to_inflict = self.my_hero.level * self.my_hero.damage

        enemy_expected_level = self.enemy_hero.level
        enemy_expected_damage = self.enemy_hero.damage
        enemy_damage_to_inflict = self.enemy_hero.level * self.enemy_hero.damage

        # Set low health values
        self.enemy_hero.health = 18

        my_expected_health = self.my_hero.health - enemy_damage_to_inflict + 5
        enemy_expected_health = self.enemy_hero.health - my_damage_to_inflict

        battle_result = self.my_hero.battle(self.enemy_hero)
        expected_result = "You win"

        self.assertEqual(battle_result, expected_result)

        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

        self.assertEqual(self.enemy_hero.level, enemy_expected_level)
        self.assertEqual(self.enemy_hero.health, enemy_expected_health)
        self.assertEqual(self.enemy_hero.damage, enemy_expected_damage)

    def test__battle__fight_enemy__expect_to_lose_and_have_updated_stats(self):
        my_expected_level = self.my_hero.level
        my_expected_damage = self.my_hero.damage
        my_damage_to_inflict = self.my_hero.level * self.my_hero.damage

        enemy_expected_level = self.enemy_hero.level + 1
        enemy_expected_damage = self.enemy_hero.damage + 5
        enemy_damage_to_inflict = self.enemy_hero.level * self.enemy_hero.damage

        # Set low health values
        self.my_hero.health = 10

        my_expected_health = self.my_hero.health - enemy_damage_to_inflict
        enemy_expected_health = self.enemy_hero.health - my_damage_to_inflict + 5

        battle_result = self.my_hero.battle(self.enemy_hero)
        expected_result = "You lose"

        self.assertEqual(battle_result, expected_result)

        self.assertEqual(self.my_hero.level, my_expected_level)
        self.assertEqual(self.my_hero.health, my_expected_health)
        self.assertEqual(self.my_hero.damage, my_expected_damage)

        self.assertEqual(self.enemy_hero.level, enemy_expected_level)
        self.assertEqual(self.enemy_hero.health, enemy_expected_health)
        self.assertEqual(self.enemy_hero.damage, enemy_expected_damage)

    def test__hero_str_method_expect_proper_string(self):
        my_hero_string_actual = str(self.my_hero)
        my_hero_string_expected = f"Hero {self.MY_USERNAME}: {self.MY_LEVEL} lvl\n" \
                                  f"Health: {self.MY_HEALTH}\n" \
                                  f"Damage: {self.MY_DAMAGE}\n"

        enemy_hero_string_actual = str(self.enemy_hero)
        enemy_hero_string_expected = f"Hero {self.ENEMY_USERNAME}: {self.ENEMY_LEVEL} lvl\n" \
                                     f"Health: {self.ENEMY_HEALTH}\n" \
                                     f"Damage: {self.ENEMY_DAMAGE}\n"

        self.assertEqual(my_hero_string_actual, my_hero_string_expected)
        self.assertEqual(enemy_hero_string_actual, enemy_hero_string_expected)


if __name__ == "__main__":
    main()
