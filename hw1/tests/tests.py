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
    @mock.patch.object(TicTacToe, "_prompt_for_input")
    @mock.patch.object(TicTacToe, "show_board")
    def test_game_start(self, mock_show_board, mock_prompt, _):
        self.game._board[0][0] = "X"
        self.game._board[1][1] = "X"
        self.game.start_game()
        mock_show_board.assert_called()
        mock_prompt.assert_called()


if __name__ == '__main__':
    unittest.main()
