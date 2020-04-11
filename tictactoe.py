"""
Tic Tac Toe Player
"""

import math
import copy

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
    x = 0
    o = 0
    for i in board:
        for j in i:
            if j != EMPTY:
                if j == X:
                    x = x + 1
                else:
                    o = o + 1
    if x <= o:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return action


# raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = copy.deepcopy(board)

    if new_board[i][j] == EMPTY:
        new_board[i][j] = player(new_board)

    return new_board


def check_horizontally(board):
    for row in board:
        flag = True
        for i in range(1, len(row)):
            if row[i] != row[i - 1]:
                flag = False
                break
        if flag is True:
            return row[2]
    return None


def check_vertically(board):
    for i in range(3):
        flag = True
        for j in range(1, 3):
            if board[j][i] != board[j - 1][i]:
                flag = False
                break

        if flag is True:
            return board[0][i]
    return None


def check_diagonally(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[1][1] == board[0][2] and board[0][2] == board[2][0]:
        return board[1][1]
    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    res = check_horizontally(board)
    if res is None:
        res = check_vertically(board)
        if res is None:
            res = check_diagonally(board)
    return res


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    return dfs(board, True)[1]


def dfs(board, is_max):
    if terminal(board):
        return utility(board), None

    if is_max:
        best_score = -math.inf
        best_action = ()
        for action in actions(board):
            new_board = result(board, action)
            res = dfs(new_board, False)
            if res[0] > best_score:
                best_score = res[0]
                best_action = action
        return best_score, best_action
    else:
        best_score = math.inf
        best_action = ()
        for action in actions(board):
            new_board = result(board, action)
            res = dfs(new_board, True)
            if res[0] > best_score:
                best_score = res[0]
                best_action = action
        return best_score, best_action


"""
0,1  =>>  1,2
0,0  =>>  0,2
2,2  =>>  2,0
"""
