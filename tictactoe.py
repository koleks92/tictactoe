"""
Tic Tac Toe Player
"""

import math, copy

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


    # Loop through each line, and each mark
    for line in board:
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

    # Loop with enumearte through board, if 'EMPTY' add to actions
    for i, j in enumerate(board):
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
    else:
        # Deepcopy of the board
        c_board = copy.deepcopy(board)
        
        # Get action indexes
        (i, j) = action

        # Get the mark and set on the board
        mark = player(board)
        c_board[i][j] = mark

        return c_board
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
        
    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != EMPTY:
            return board[0][column]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    # If no winner
    return None
 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) == 0 or winner(board) == X or winner(board) == O:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    else:
        return None
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    else:
        

