"""Main file with all functionality of the Tic-Tac-Toe game"""
from typing import Tuple

from .exceptions import TicTacToeGameFinished, TicTacToeBadInput


class TicTacToe:
    """Base class for Tic Tac Toe game"""
    CROSS_CHAR = "X"
    NOUGHT_CHAR = "O"
    WIN_CROSS_CHAR = "Ӿ"
    WIN_NOUGHT_CHAR = "θ"

    def __init__(self, board_size: int = 3):
        self._board_size = board_size
        self._board = [[" " for _ in range(self._board_size)]
                       for _ in range(self._board_size)]
        self._num_border_line \
            = "  " \
              + ("  {} " * self._board_size).format(*range(self._board_size))
        self._border_line = "  " + ("+---" * self._board_size + "+")
        self._board_line = "| {} " * self._board_size + "|"
        # list of tuples: (row_pos, col_pos)
        self._game_log = []
        self._is_first_player_turn = True
        self._current_turn_num = 0
        self._version = "0.0.1"

    def show_board(self):
        """Show Tic Tac Toe board in cli"""
        print(self._num_border_line)
        for idx, row in enumerate(self._board):
            print(self._border_line)
            print(str(idx) + " " + self._board_line.format(*row))
        print(self._border_line)

    def _validate_input(self, input_str: str) -> Tuple[int, int]:
        """Validate user input"""
        try:
            row_pos, col_pos = map(int, input_str.split())
        except ValueError as val_err:
            raise TicTacToeBadInput(
                f"row_pos and col_pos should be spaced int numbers "
                f"like this: 1 0, but got this: {input_str}"
            ) from val_err
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
                "This position on the board is already full filled. "
                "Try another board position."
            )
        return row_pos, col_pos

    def _set_turn(self, row_pos: int, col_pos: int):
        self._board[row_pos][col_pos] \
            = self.CROSS_CHAR \
            if self._is_first_player_turn \
            else self.NOUGHT_CHAR
        play = (
            row_pos,
            col_pos,
        )
        self._game_log.append(play)
        # change turn
        self._is_first_player_turn = not self._is_first_player_turn
        self._current_turn_num += 1

    def _win(self, win_type: str, **kwargs):
        """In case if somebody has won"""
        if win_type == "diag":
            crossed_out_char = \
                self.WIN_CROSS_CHAR \
                if self.CROSS_CHAR == self._board[0][0] \
                else self.WIN_NOUGHT_CHAR
            for i in range(self._board_size):
                self._board[i][i] = crossed_out_char
        elif win_type == "antidiag":
            crossed_out_char = \
                self.WIN_CROSS_CHAR \
                if self.CROSS_CHAR == self._board[self._board_size - 1][0] \
                else self.WIN_NOUGHT_CHAR
            for i in range(self._board_size):
                self._board[i][self._board_size - i - 1] = crossed_out_char
        elif win_type == "row":
            crossed_out_char = \
                self.WIN_CROSS_CHAR \
                if self.CROSS_CHAR == self._board[kwargs["row_idx"]][0] \
                else self.WIN_NOUGHT_CHAR
            for j in range(self._board_size):
                self._board[kwargs["row_idx"]][j] = crossed_out_char
        elif win_type == "col":
            crossed_out_char = \
                self.WIN_CROSS_CHAR \
                if self.CROSS_CHAR == self._board[0][kwargs["col_idx"]] \
                else self.WIN_NOUGHT_CHAR
            for i in range(self._board_size):
                self._board[i][kwargs["col_idx"]] = crossed_out_char
        char = self.NOUGHT_CHAR \
            if self._is_first_player_turn \
            else self.CROSS_CHAR
        player_id = 2 if self._is_first_player_turn else 1
        raise TicTacToeGameFinished(
            f"Game finished. "
            f"Player #{player_id} and '{char}' wins!"
        )

    @staticmethod
    def _draw():
        """In case if it had been a draw"""
        print("It's a draw. No one wins!")

    def _greetings(self):
        """Greet user before game start"""
        greet = (
            f"Welcome to TicTacToe game v{self._version}\n"
            f"Each player should use this turn notation: "
            f"row_pos col_pos.\n"
            f"Example#1: 0 1\n"
            f"Example#2: 1 2\n"
            f"row_pos & col_pos starts from 0.\n"
            f"First player starts with '{self.CROSS_CHAR}', "
            f"second - '{self.NOUGHT_CHAR}'.\n"
        )
        print(greet)

    def _prompt_for_input(self):
        """Prompt for input before each iteration of the game"""
        player_id = 1 if self._is_first_player_turn else 2
        prompt_str = f"Player#{player_id}, your turn:"
        print(prompt_str)

    def _check_winner(self):
        """Check if we have a winner"""
        statistics = {
            "X": {
                "row": [
                    0 for _ in range(self._board_size)
                ],  # X stats for every row
                "col": [
                    0 for _ in range(self._board_size)
                ],  # X stats for every col
                "diag": 0,
                "antidiag": 0,
            },
            "O": {
                "row": [
                    0 for _ in range(self._board_size)
                ],  # O stats for every row
                "col": [
                    0 for _ in range(self._board_size)
                ],  # O stats for every col
                "diag": 0,
                "antidiag": 0,
            },
        }
        for i in range(self._board_size):
            for j in range(self._board_size):
                if self.CROSS_CHAR == self._board[i][j]:
                    if i == j:
                        statistics["X"]["diag"] += 1
                        if self._board_size == statistics["X"]["diag"]:
                            self._win("diag")
                    if i + j == self._board_size - 1:
                        statistics["X"]["antidiag"] += 1
                        if self._board_size == statistics["X"]["antidiag"]:
                            self._win("antidiag")
                    statistics["X"]["row"][i] += 1
                    if self._board_size == statistics["X"]["row"][i]:
                        self._win("row", row_idx=i)
                    statistics["X"]["col"][j] += 1
                    if self._board_size == statistics["X"]["col"][j]:
                        self._win("col", col_idx=j)
                elif self.NOUGHT_CHAR == self._board[i][j]:
                    if i == j:
                        statistics["O"]["diag"] += 1
                        if self._board_size == statistics["O"]["diag"]:
                            self._win("diag")
                    if i + j == self._board_size - 1:
                        statistics["O"]["antidiag"] += 1
                        if self._board_size == statistics["O"]["antidiag"]:
                            self._win("antidiag")
                    statistics["O"]["row"][i] += 1
                    if self._board_size == statistics["O"]["row"][i]:
                        self._win("row", row_idx=i)
                    statistics["O"]["col"][j] += 1
                    if self._board_size == statistics["O"]["col"][j]:
                        self._win("col", col_idx=j)

    def start_game(self):
        """Game main loop"""
        self._greetings()
        while len(self._game_log) < self._board_size ** 2:
            self.show_board()
            self._prompt_for_input()
            user_input = input()
            try:
                row_pos, col_pos = self._validate_input(user_input)
                self._set_turn(row_pos, col_pos)
                self._check_winner()
            except TicTacToeBadInput as bad_input_e:
                print(str(bad_input_e))
                continue
            except TicTacToeGameFinished as game_finished_e:
                print(str(game_finished_e))
                self.show_board()
                break
        if len(self._game_log) >= self._board_size ** 2 \
                and len(self._game_log) > 1:
            self._draw()
            self.show_board()
