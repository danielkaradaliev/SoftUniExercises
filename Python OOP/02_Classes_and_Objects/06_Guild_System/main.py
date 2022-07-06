from project.guild import Guild
from project.player import Player


def main():
    player = Player("George", 50, 100)
    print(player.add_skill("Shield Break", 20))
    print(player.player_info())
    guild = Guild("UGT")
    print(guild.assign_player(player))
    print(guild.guild_info())


if __name__ == '__main__':
    main()
