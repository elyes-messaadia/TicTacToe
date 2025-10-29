# Plateau + règles (gagnant, nul, coups dispo, affichage, etc.)

# board.py
# -----------
# Board representation and core game rules.

from typing import List, Optional

# Représentation: liste de 9 éléments (None, 'X' ou 'O')
Board = List[Optional[str]]

# lignes gagnantes (trois en lignes)
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # lignes
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colonnes
    (0, 4, 8), (2, 4, 6),             # diagonales
]


def print_board(board: Board) -> None:
    """Affiche le plateau 3x3. Les cases vides sont numérotées 1..9."""
    def cell(i: int) -> str:
        return board[i] if board[i] is not None else str(i + 1)

    for r in range(3):
        start = r * 3
        print(f" {cell(start)} | {cell(start+1)} | {cell(start+2)} ")
        if r < 2:
            print("---+---+---")
    print()


def check_winner(board: Board) -> Optional[str]:
    """Retourne 'X' ou 'O' si l'un gagne, sinon None."""
    for a, b, c in WIN_LINES:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    """Vrai si toutes les cases sont remplies et qu'il n'y a pas de gagnant."""
    return all(cell is not None for cell in board) and check_winner(board) is None


def available_moves(board: Board) -> List[int]:
    """Indices des cases libres (0..8)."""
    return [i for i, cell in enumerate(board) if cell is None]


def make_move(board: Board, index: int, sign: str) -> bool:
    """Essaye de jouer 'sign' sur 'index'. Retourne True si réussi."""
    if not (0 <= index <= 8):
        return False
    if board[index] is not None:
        return False
    if sign not in ("X", "O"):
        return False
    board[index] = sign
    return True
