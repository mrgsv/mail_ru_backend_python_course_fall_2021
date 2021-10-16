"""Exceptions for Tic-Tac-Toe game"""


class TicTacToeException(Exception):
    """Base exception for Tic Tac Toe"""


class TicTacToeGameFinished(TicTacToeException):
    """Exception if game is finished"""


class TicTacToeBadInput(TicTacToeException):
    """Exception if input is bad"""
