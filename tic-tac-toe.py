spiel_active = True
current_player = "X"

game_board = [" ",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"
            ]

def print_board():
    """Prints the current state of the game board."""
    print(game_board[1] + "|" + game_board[2] + "|" + game_board[3])
    print(game_board[4] + "|" + game_board[5] + "|" + game_board[6])
    print(game_board[7] + "|" + game_board[8] + "|" + game_board[9])


def player_input():
    """Handles player input for making a move."""
    global spiel_active
    while True:
        move = input("Please enter a position: ")

        if move == "q":
            spiel_active = False
            return

        try:
            move = int(move)
        except ValueError:
            print("Please enter a number from 1 to 9.")
        else:
            if 1 <= move <= 9:
                if game_board[move] == "X" or game_board[move] == "O":
                    print("That position is already taken. Choose another!")
                else:
                    return move
            else:
                print("Number must be between 1 and 9!")


def switch_player():
    """Switches the current player between 'X' and 'O'."""
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_win():
    """Checks if any player has won the game."""
    if game_board[1] == game_board[2] == game_board[3]:
        return game_board[1]
    if game_board[4] == game_board[5] == game_board[6]:
        return game_board[4]
    if game_board[7] == game_board[8] == game_board[9]:
        return game_board[7]

    if game_board[1] == game_board[4] == game_board[7]:
        return game_board[1]
    if game_board[2] == game_board[5] == game_board[8]:
        return game_board[2]
    if game_board[3] == game_board[6] == game_board[9]:
        return game_board[3]

    if game_board[1] == game_board[5] == game_board[9]:
        return game_board[5]
    if game_board[7] == game_board[5] == game_board[3]:
        return game_board[5]


def check_draw():
    """Checks if the game ended in a draw."""
    if all(cell == "X" or cell == "O" for cell in game_board[1:]):
        return "draw"


print_board()

while spiel_active:
    print()
    print("Player " + current_player + "'s turn")
    move = player_input()
    if move:
        game_board[move] = current_player
        print_board()
        winner = check_win()
        if winner:
            print("Player " + winner + " wins!")
            break
        draw = check_draw()
        if draw:
            print("The game ends in a draw.")
            break
        switch_player()
