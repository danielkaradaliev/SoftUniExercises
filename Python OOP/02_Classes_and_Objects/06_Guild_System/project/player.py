class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        linesep = "\n"
        info = f"Name: {self.name}{linesep}Guild: {self.guild}{linesep}HP: {self.hp}{linesep}MP: {self.mp}{linesep}" + \
            linesep.join([f"==={skill} - {mana_cost}" for skill, mana_cost in self.skills.items()])
        return info
