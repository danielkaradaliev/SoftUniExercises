MATRIX_SIZE = 6

player_is_resting = {
    "Tom": False,
    "Jerry": False
}


def get_opponent_player(player):
    return "Jerry" if player == "Tom" else "Tom"


players = [x for x in input().split(", ")]
my_matrix = []
is_game_over = False

for _ in range(MATRIX_SIZE):
    my_matrix.append([x for x in input().split()])

while not is_game_over:
    for player in players:
        if not is_game_over:
            coord_x, coord_y = [int(x) for x in input().strip("()").split(", ")]
            if player_is_resting[player]:
                player_is_resting[player] = False
                continue

            symbol = my_matrix[coord_x][coord_y]
            if symbol == "E":
                is_game_over = True
                print(f"{player} found the Exit and wins the game!")
            elif symbol == "T":
                is_game_over = True
                winner = get_opponent_player(player)
                print(f"{player} is out of the game! The winner is {winner}.")
            elif symbol == "W":
                player_is_resting[player] = True
                print(f"{player} hits a wall and needs to rest.")
