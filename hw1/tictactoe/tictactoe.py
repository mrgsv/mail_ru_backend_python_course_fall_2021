from typing import Tuple

from .exceptions import TicTacToeGameFinished, TicTacToeBadInput


class TicTacToe:
    """Base class for Tic Tac Toe game"""
    CROSS_CHAR = "X"
    NOUGHT_CHAR = "O"

    def __init__(self, board_size: int = 3):
        self._board_size = board_size
        self._board = [[" " for _ in range(self._board_size)]
                       for _ in range(self._board_size)]
        self._border_line = "+---" * self._board_size + "+"
        self._board_line = "| {} " * self._board_size + "|"
        self._game_log = []

    def _show_board(self):
        """Show Tic Tac Toe board in cli"""
        for row in self._board:
            print(self._border_line)
            print(self._board_line.format(*row))
        print(self._border_line)

    def _validate_input(self, input_str: str) -> Tuple[str, int, int]:
        """Validate user input"""
        input_params = input_str.split()
        if len(input_params) != 3:
            raise TicTacToeBadInput(
                f"Expected input in this way: char row_pos col_pos, "
                f"but got: {input_str}"
            )
        char = input_params[0]
        row_pos = int(input_params[1])
        col_pos = int(input_params[2])
        if char not in (TicTacToe.CROSS_CHAR, TicTacToe.NOUGHT_CHAR):
            raise TicTacToeBadInput(
                f"Expected {TicTacToe.CROSS_CHAR} or {TicTacToe.NOUGHT_CHAR}, "
                f"but got: {char}"
            )
        if row_pos < 0 or row_pos >= self._board_size:
            raise TicTacToeBadInput(
                f"Expected row_pos in [0, {self._board_size}), "
                f"but got: {row_pos}"
            )
        if col_pos < 0 or col_pos >= self._board_size:
            raise TicTacToeBadInput(
                f"Expected col_pos in [0, {self._board_size}), "
                f"but got: {col_pos}"
            )
        if self._board[row_pos][col_pos] != " ":
            raise TicTacToeBadInput(
                f"This position on the board is already full filled. "
                f"Try another board position."
            )
        return char, row_pos, col_pos

    def _win(self):
        """In case if somebody has won"""
        pass

    def _draw(self):
        """In case if it had been a draw"""
        pass

    def _greetings(self):
        """Greet user before game start"""
        pass

    def _prompt_for_input(self):
        """Prompt for input before each iteration of the game"""
        pass

    def _check_winner(self):
        """Check if we have a winner"""
        pass

    def start_game(self):
        """Game main loop"""
        self._greetings()
        while len(self._game_log) < self._board_size ** 2:
            self._prompt_for_input()
            self._show_board()
            user_input = input()
            try:
                char, row_pos, col_pos = self._validate_input(user_input)
            except TicTacToeBadInput as bad_input_e:
                print(str(bad_input_e))
                continue
