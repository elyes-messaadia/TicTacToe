"""Board utilities minimalistes pour Tic Tac Toe.

Le plateau est une liste de 9 éléments valant None (case vide), 'X' ou 'O'.
Fonctions documentées en français pour faciliter la prise en main.
"""
from typing import List, Optional

Board = List[Optional[str]]

WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def new_board() -> Board:
    """Retourne un plateau vierge : liste de 9 None."""
    return [None] * 9


def print_board(board: Board) -> None:
    """Affiche le plateau. Les cases vides montrent 1..9 pour l'entrée humaine."""
    def cell(i: int) -> str:
        return board[i] if board[i] is not None else str(i + 1)
    for r in range(3):
        i = r * 3
        print(f" {cell(i)} | {cell(i+1)} | {cell(i+2)} ")
        if r < 2:
            print("---+---+---")


def available_moves(board: Board) -> List[int]:
    """Retourne la liste des indices libres (0..8)."""
    return [i for i, v in enumerate(board) if v is None]


def make_move(board: Board, index: int, sign: str) -> bool:
    """Joue 'sign' en 'index' si légal (0<=index<9, case vide, sign en X/O).

    Retourne True si le coup a été joué, False sinon.
    """
    if sign not in ("X", "O") or not (0 <= index < 9) or board[index] is not None:
        return False
    board[index] = sign
    return True


def check_winner(board: Board) -> Optional[str]:
    """Retourne 'X' ou 'O' si l'un gagne; None sinon."""
    for a, b, c in WIN_LINES:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    """Vrai si toutes les cases sont remplies et qu'il n'y a pas de gagnant."""
    return all(cell is not None for cell in board) and check_winner(board) is None
