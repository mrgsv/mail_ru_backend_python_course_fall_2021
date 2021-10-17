import unittest
from unittest import mock

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

    # TODO: update this test
    @mock.patch("builtins.input", side_effect=["2 2\n"])
    @mock.patch.object(TicTacToe, "_greetings")
    def test_game_start(self, mock_, _):
        self.game._board[0][0] = "X"
        self.game._board[1][1] = "X"
        self.game.start_game()
        mock_.assert_called("_greetings")


if __name__ == '__main__':
    unittest.main()
