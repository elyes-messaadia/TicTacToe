# Fonction ia(board, signe) + helpers
# ai.py
# ------
# The required AI function: ia(board, signe) -> int | False

from typing import Optional, Union
from board import Board, available_moves, check_winner

def _try_winning_move(board: Board, sign: str) -> Optional[int]:
    """
    If there exists a move that lets 'sign' win immediately, return its index.
    Otherwise return None.

    Pattern:
    - Simulate placing 'sign' in each free cell
    - If it makes a 3-in-a-row, that's the winning move
    - Revert after testing
    """
    for i in available_moves(board):
        board[i] = sign
        if check_winner(board) == sign:
            board[i] = None
            return i
        board[i] = None
    return None


def ia(board: Board, signe: str) -> Union[int, bool]:
    """
    Decision-making AI for Tic Tac Toe.

    Parameters
    ----------
    board : list of length 9 with values in {'X','O',None}
    signe : 'X' or 'O' (the AI's symbol)

    Returns
    -------
    int  : the chosen index (0..8)
    bool : False on invalid inputs or if no legal moves exist

    Strategy (explainable and deterministic):
    1) Win now if possible.
    2) Otherwise block opponent's immediate win.
    3) Take center if free.
    4) Take a corner (0,2,6,8) if free.
    5) Take a side (1,3,5,7).
    """
    # --- Validate inputs ---
    if signe not in ('X', 'O'):
        return False
    if not isinstance(board, list) or len(board) != 9:
        return False
    for cell in board:
        if cell not in (None, 'X', 'O'):
            return False

    opponent = 'O' if signe == 'X' else 'X'
    moves = available_moves(board)
    if not moves:
        return False

    # 1) Try to win immediately
    win_idx = _try_winning_move(board, signe)
    if win_idx is not None:
        return win_idx

    # 2) Block opponent's immediate win
    block_idx = _try_winning_move(board, opponent)
    if block_idx is not None:
        return block_idx

    # 3) Take center
    if 4 in moves:
        return 4

    # 4) Take a corner
    for corner in (0, 2, 6, 8):
        if corner in moves:
            return corner

    # 5) Take a side
    for side in (1, 3, 5, 7):
        if side in moves:
            return side

    # Fallback: should not happen given checks
    return moves[0]
