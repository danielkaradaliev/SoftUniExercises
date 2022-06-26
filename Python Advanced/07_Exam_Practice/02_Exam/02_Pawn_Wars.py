MOVES = {
    "White": (-1, 0),
    "Black": (1, 0)
}

QUEENING_RANK = {
    "White": 0,
    "Black": 7
}

CAPTURE_MOVES = {
    "White": ((-1, -1), (-1, 1)),
    "Black": ((1, -1), (1, 1))
}

BOARD_SIZE = 8
RANK_MAP = dict({x: abs(x - BOARD_SIZE) for x in range(BOARD_SIZE)})
COLUMN_MAP = dict({x: str(chr(97 + x)) for x in range(BOARD_SIZE)})


def get_pawn_position(matrix, pawn):
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if matrix[row_index][col_index] == pawn:
                return [row_index, col_index]


def get_opponent_pawn(pawn):
    return "Black" if pawn == "White" else "White"


def can_capture(pawn_x, pawn_y, pawn):
    opponent_pawn = get_opponent_pawn(pawn)
    opponent_pawn_x, opponent_pawn_y = pawns_dict[opponent_pawn]

    for capture_move in CAPTURE_MOVES[pawn]:
        capture_x, capture_y = pawn_x + capture_move[0], pawn_y + capture_move[1]
        if capture_x in range(BOARD_SIZE) and capture_y in range(BOARD_SIZE):
            if capture_x == opponent_pawn_x and capture_y == opponent_pawn_y:
                return True, capture_x, capture_y
    return False, None, None


def pawn_move(pawn_x, pawn_y, pawn):
    return [pawn_x + MOVES[pawn][0], pawn_y + MOVES[pawn][1]]


def get_board_square(pawn_x, pawn_y):
    square_column = COLUMN_MAP[pawns_dict[pawn][1]]
    square_rank = str(RANK_MAP[pawns_dict[pawn][0]])
    return square_column + square_rank


board = []
is_game_over = False

for _ in range(BOARD_SIZE):
    board.append([x for x in input().split()])

pawns_dict = {
    "White": get_pawn_position(board, "w"),
    "Black": get_pawn_position(board, "b")
}

while not is_game_over:
    for pawn, matrix_square in pawns_dict.items():
        if not is_game_over:
            pawn_x, pawn_y = matrix_square

            can_capture_info = can_capture(pawn_x, pawn_y, pawn)
            if can_capture_info[0]:
                capture_x, capture_y = can_capture_info[1:]
                pawns_dict[pawn] = [capture_x, capture_y]
                is_game_over = True
                board_square = get_board_square(capture_x, capture_y)
                print(f"Game over! {pawn} win, capture on {board_square}.")
            else:
                pawn_x, pawn_y = pawn_move(pawn_x, pawn_y, pawn)
                pawns_dict[pawn] = [pawn_x, pawn_y]

                if pawn_x == QUEENING_RANK[pawn]:
                    is_game_over = True
                    board_square = get_board_square(pawn_x, pawn_y)
                    print(f"Game over! {pawn} pawn is promoted to a queen at {board_square}.")
