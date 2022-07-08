from project.hero import Hero
from project.elf import Elf
from project.wizard import Wizard
from project.knight import Knight
from project.muse_elf import MuseElf
from project.dark_wizard import DarkWizard
from project.dark_knight import DarkKnight
from project.soul_master import SoulMaster
from project.blade_knight import BladeKnight


def main():
    hero1 = Hero("H", 1)
    print(hero1.username)
    print(hero1.level)
    print(str(hero1))
    print(hero1.__class__.__bases__[0].__name__)

    hero2 = Elf("Elf", 2)
    print(hero2.username)
    print(hero2.level)
    print(str(hero2))
    print(hero2.__class__.__bases__[0].__name__)

    hero3 = MuseElf("MuseElf", 3)
    print(hero3.username)
    print(hero3.level)
    print(str(hero3))
    print(hero3.__class__.__bases__[0].__name__)

    hero4 = Wizard("Wizard", 4)
    print(hero4.username)
    print(hero4.level)
    print(str(hero4))
    print(hero4.__class__.__bases__[0].__name__)

    hero5 = DarkWizard("Dark Wizard", 5)
    print(hero5.username)
    print(hero5.level)
    print(str(hero5))
    print(hero5.__class__.__bases__[0].__name__)

    hero6 = SoulMaster("Soul Master", 6)
    print(hero6.username)
    print(hero6.level)
    print(str(hero6))
    print(hero6.__class__.__bases__[0].__name__)

    hero7 = Knight("Knight", 7)
    print(hero7.username)
    print(hero7.level)
    print(str(hero7))
    print(hero7.__class__.__bases__[0].__name__)

    hero8 = DarkKnight("Dark Knight", 8)
    print(hero8.username)
    print(hero8.level)
    print(str(hero8))
    print(hero8.__class__.__bases__[0].__name__)

    hero9 = BladeKnight("Blade Knight", 9)
    print(hero9.username)
    print(hero9.level)
    print(str(hero9))
    print(hero9.__class__.__bases__[0].__name__)


if __name__ == "__main__":
    main()
