from project.horse_race_app import HorseRaceApp


def main():
    horse_race_app = HorseRaceApp()
    print(horse_race_app.add_horse("Appaloosa", "Spirit", 80))
    print(horse_race_app.add_horse("Thoroughbred", "Rocket", 110))
    print(horse_race_app.add_jockey("Peter", 19))
    print(horse_race_app.add_jockey("Mariya", 21))
    print(horse_race_app.create_horse_race("Summer"))
    print(horse_race_app.add_horse_to_jockey("Peter", "Appaloosa"))
    print(horse_race_app.add_horse_to_jockey("Peter", "Thoroughbred"))
    print(horse_race_app.add_horse_to_jockey("Mariya", "Thoroughbred"))
    print(horse_race_app.add_jockey_to_horse_race("Summer", "Mariya"))
    print(horse_race_app.add_jockey_to_horse_race("Summer", "Peter"))
    print(horse_race_app.add_jockey_to_horse_race("Summer", "Mariya"))
    print(horse_race_app.start_horse_race("Summer"))


if __name__ == "__main__":
    main()
