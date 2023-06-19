"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Create varable to count the turn
    xs = 0
    os = 0
    emptys = 0

    # Initiate the board
    board_state = board()

    # Loop through each line, and each mark
    for line in board_state:
        for m in line:
            if m == X:
                xs += 1
            if m == O:
                os += 1
            if m == EMPTY:
                emptys += 1

    if emptys == 9:
        return X
    if xs > os:
        return O
    if os == xs:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create state and initiate board
    actions = set()
    board_state = board()

    # Loop with enumarte thourgh board, if 'EMPTY' add to actions
    for i, j in enumerate(board_state):
        for k, l in enumerate(j):
            if l == EMPTY:
                actions.add((i, k))

    return actions
                


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
