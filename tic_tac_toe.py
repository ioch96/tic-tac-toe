"""
This module contains the implementation of a simple Tic-Tac-Toe game.
"""

class TicTacToe:
    """Represents a Tic-Tac-Toe game.

    Manages the game board, player turns, and checks for game outcomes such as wins and draws.
    """
    def __init__(self):
        self.game_active = True
        self.current_player = "X"
        self.game_board = [" ",
                           "1", "2", "3",
                           "4", "5", "6",
                           "7", "8", "9"
                          ]

    def print_board(self):
        """Prints the current state of the game board."""
        print(self.game_board[1] + "|" + self.game_board[2] + "|" + self.game_board[3])
        print(self.game_board[4] + "|" + self.game_board[5] + "|" + self.game_board[6])
        print(self.game_board[7] + "|" + self.game_board[8] + "|" + self.game_board[9])

    def player_input(self):
        """Handles player input for making a move.

        Prompts the user to enter a position on the game board. 
        Validates the input to ensure it is a number between 1 and 9, and 
        checks that the position is not already taken. Allows the user to quit
        the game by entering 'q'.
        
        Returns:
            int or None: The position chosen by the player, or None if the player quits.
        """
        while True:
            move = input("Please enter a position: ")

            if move == "q":
                self.game_active = False
                return None

            try:
                move = int(move)
            except ValueError:
                print("Please enter a number from 1 to 9.")
            else:
                if 1 <= move <= 9:
                    if self.game_board[move] in {"X", "O"}:
                        print("That position is already taken. Choose another!")
                    else:
                        return move
                else:
                    print("Number must be between 1 and 9!")

    def switch_player(self):
        """Switches the current player between 'X' and 'O'."""
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self):
        """Checks if any player has won the game.

        Evaluates the game board to determine if there is a winning combination.
        
        Returns:
            str or None: The symbol of the winning player or None if there is no winner.
        """
        winning_combinations = [
            (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            (1, 4, 7),
            (2, 5, 8),
            (3, 6, 9),
            (1, 5, 9),
            (7, 5, 3)
        ]

        for a, b, c in winning_combinations:
            if self.game_board[a] == self.game_board[b] == self.game_board[c]:
                return self.game_board[a]

        return None

    def check_draw(self):
        """Checks if the game ended in a draw.

        Evaluates if all positions on the game board are filled and no winner is found.
        
        Returns:
            str or None: 'draw' if the game is a draw, otherwise None.
        """
        if all(cell in {"X", "O"} for cell in self.game_board[1:]):
            return "draw"
        return None

    def main(self):
        """Main function to start and run the Tic-Tac-Toe game.

        Coordinates the flow of the game, including handling player turns, 
        checking for wins or draws, and switching players.
        """
        self.print_board()

        while self.game_active:
            print()
            print("Player " + self.current_player + "'s turn")
            move = self.player_input()
            if move is not None:
                self.game_board[move] = self.current_player
                self.print_board()
                winner = self.check_win()
                if winner:
                    print("Player " + winner + " wins!")
                    break
                draw = self.check_draw()
                if draw:
                    print("The game ends in a draw.")
                    break
                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
