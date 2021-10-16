"""Entrypoint for CLI Tic-Tac-Toe"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from tictactoe import TicTacToe


DEFAULT_BOARD_SIZE = 3


def main():
    """Main CLI interface"""
    parser = ArgumentParser(
        prog="Tic-Tac-Toe game",
        description="CLI Tic-Tac-Toe game",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n", "--board_size",
        dest="board_size",
        default=DEFAULT_BOARD_SIZE,
        help="Board size for the game",
    )
    arguments = parser.parse_args()
    game = TicTacToe(board_size=int(arguments.board_size))
    game.start_game()


if __name__ == '__main__':
    main()
