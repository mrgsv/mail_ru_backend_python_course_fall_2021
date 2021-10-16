import unittest

from ..tictactoe import TicTacToe
from ..tictactoe.exceptions import TicTacToeBadInput


class TestTicTacToe(unittest.TestCase):
    def setUp(self) -> None:
        self.game = TicTacToe(board_size=3)

    def test_validate_input(self):
        with self.assertRaises(TicTacToeBadInput):
            self.game._validate_input("abc")

    def test_board(self):
        self.assertEqual(self.game._board,
                         [[" " for _ in range(self.game._board_size)]
                          for _ in range(self.game._board_size)])

    def test_game_start(self):
        # TODO: write test here
        pass


if __name__ == '__main__':
    unittest.main()
