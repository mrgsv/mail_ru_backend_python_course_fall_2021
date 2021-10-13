class TicTacToeException(Exception):
    """Base exception for Tic Tac Toe"""
    pass


class TicTacToeGameFinished(TicTacToeException):
    """Exception if game is finished"""
    pass


class TicTacToeBadInput(TicTacToeException):
    """Exception if input is bad"""
    pass
