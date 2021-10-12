from .exceptions import TicTacToeGameFinished


class TicTacToe:
    """Base class for Tic Tac Toe game"""

    def __init__(self, board_size: int = 3):
        self._board_size = board_size
        self._board = [[" " for _ in range(self._board_size)]
                       for _ in range(self._board_size)]
        self._border_line = "+---" * self._board_size + "+"
        self._board_line = "| {} " * self._board_size + "|"
        self._game_log = []

    def show_board(self):
        """Show Tic Tac Toe board in cli"""
        for row in self._board:
            print(self._border_line)
            print(self._board_line.format(*row))
        print(self._border_line)

    def validate_input(self):
        pass

    def _win(self):
        pass

    def _draw(self):
        pass

    def start_game(self):
        for game_round in range(self._board_size ** 2):
            self._win()
        else:
            self._draw()

    def check_winner(self):
        pass
