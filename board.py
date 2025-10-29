# Plateau + règles (gagnant, nul, coups dispo, affichage, etc.)

# board.py
# -----------
# Board representation and core game rules.

from typing import List, Optional

# The board is a flat list of 9 cells:
# indices:  0 | 1 | 2
#           3 | 4 | 5
#           6 | 7 | 8
# Each cell contains: 'X', 'O', or None.
Board = List[Optional[str]]

# All possible 3-in-a-row lines (rows, columns, diagonals)
WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def print_board(board: Board) -> None:
    """
    Display the board in a human-readable 3x3 grid.

    For empty cells, we show 1..9 indices so the player can pick a move quickly.
    """
    def cell(i: int) -> str:
        return board[i] if board[i] is not None else str(i + 1)

    row0 = f" {cell(0)} | {cell(1)} | {cell(2)} "
    row1 = f" {cell(3)} | {cell(4)} | {cell(5)} "
    row2 = f" {cell(6)} | {cell(7)} | {cell(8)} "
    sep  = "---+---+---"
    print(row0)
    print(sep)
    print(row1)
    print(sep)
    print(row2)
    print()


def check_winner(board: Board) -> Optional[str]:
    """
    Return 'X' if X wins, 'O' if O wins, or None otherwise.

    Implementation:
    - Iterate all winning triplets.
    - If the 3 cells are equal and not None, we have a winner.
    """
    for a, b, c in WIN_LINES:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_draw(board: Board) -> bool:
    """
    Return True if all cells are filled and there is no winner.
    """
    return all(cell is not None for cell in board) and check_winner(board) is None


def available_moves(board: Board) -> List[int]:
    """
    Return a list of indices (0..8) that are currently empty.
    """
    return [i for i, cell in enumerate(board) if cell is None]


def make_move(board: Board, index: int, sign: str) -> bool:
    """
    Place 'sign' at 'index' (0..8) if legal. Return True if success, else False.

    Defensive checks:
    - Index must be in range
    - Cell must be empty
    - Sign must be 'X' or 'O'
    """
    if index < 0 or index > 8:
        return False
    if board[index] is not None:
        return False
    if sign not in ('X', 'O'):
        return False
    board[index] = sign
    return True
