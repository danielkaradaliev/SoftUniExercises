class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = list()

    def assign_player(self, player):
        if player.name in [x.name for x in self.players]:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for index, player in enumerate(self.players):
            if player_name == player.name:
                self.players.pop(index)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        linesep = "\n"
        info = f"Guild: {self.name}{linesep}" + linesep.join([player.player_info() for player in self.players])
        return info
