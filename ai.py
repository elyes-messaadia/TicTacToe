# Fonction ia(board, signe) + helpers
# ai.py
# ------
# The required AI function: ia(board, signe) -> int | False

from typing import Optional, Union
from board import Board, available_moves, check_winner


def _try_winning_move(board: Board, sign: str) -> Optional[int]:
    """Teste chaque coup libre et retourne l'index qui donne la victoire si trouvé."""
    for i in available_moves(board):
        board[i] = sign
        if check_winner(board) == sign:
            board[i] = None
            return i
        board[i] = None
    return None


def ia(board: Board, sign: str) -> Union[int, bool]:
    """IA déterministe simple : gagne si possible, bloque, puis centre/corner/side."""
    # validation minimale
    if sign not in ("X", "O"):
        return False
    if not isinstance(board, list) or len(board) != 9:
        return False
    if any(cell not in (None, "X", "O") for cell in board):
        return False

    moves = available_moves(board)
    if not moves:
        return False

    opponent = "O" if sign == "X" else "X"

    # 1) gagner tout de suite
    win = _try_winning_move(board, sign)
    if win is not None:
        return win

    # 2) bloquer l'adversaire
    block = _try_winning_move(board, opponent)
    if block is not None:
        return block

    # 3) centre
    if 4 in moves:
        return 4

    # 4) coin
    for idx in (0, 2, 6, 8):
        if idx in moves:
            return idx

    # 5) côté
    for idx in (1, 3, 5, 7):
        if idx in moves:
            return idx

    return moves[0]
