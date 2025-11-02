"""IA pour Tic Tac Toe.

Fonction principale : ia(board, sign) -> int|False.
Retourne l'indice (0..8) du meilleur coup via minimax simple (explorable) ou False
si les entrées sont invalides ou s'il n'y a pas de coup.
"""
from typing import Optional, Union
from board import Board, available_moves, check_winner


def _minimax(board: Board, player: str, ai_sign: str) -> int:
    """Minimax récursif renvoyant un score depuis la position courante.

    Retour : +1 si `ai_sign` gagne depuis cette position,
             -1 si `ai_sign` perd,
              0 si égalité possible ou position neutre.

    La fonction modifie temporairement `board` (pose un coup), appelle
    récursivement puis restaure la case à None.
    """
    # cas terminal : victoire d'un camp
    winner = check_winner(board)
    if winner == ai_sign:
        return 1
    if winner is not None:
        return -1

    # si plus de coups possibles -> match nul
    moves = available_moves(board)
    if not moves:
        return 0

    # Si c'est au tour de l'IA, on cherche à maximiser le score
    if player == ai_sign:
        best = -2
        for m in moves:
            # simule le coup
            board[m] = player
            score = _minimax(board, 'O' if player == 'X' else 'X', ai_sign)
            # restaure la case
            board[m] = None
            if score > best:
                best = score
                # coup gagnant : on peut arrêter la recherche
                if best == 1:
                    break
        return best

    # Sinon l'adversaire joue : on suppose qu'il minimise le score
    worst = 2
    for m in moves:
        board[m] = player
        score = _minimax(board, 'O' if player == 'X' else 'X', ai_sign)
        board[m] = None
        if score < worst:
            worst = score
            if worst == -1:
                break
    return worst


def ia(board: Board, sign: str) -> Union[int, bool]:
    """Choisit le meilleur coup pour `sign` en utilisant minimax.

    Validation des entrées : renvoie False si input invalide ou s'il n'y a
    aucun coup disponible.
    """
    # validation simple des paramètres
    if sign not in ("X", "O") or not isinstance(board, list) or len(board) != 9:
        return False
    if any(cell not in (None, "X", "O") for cell in board):
        return False

    moves = available_moves(board)
    if not moves:
        return False

    # évalue chaque coup possible et retient le meilleur
    best_move: Optional[int] = None
    best_score = -2
    opponent = 'O' if sign == 'X' else 'X'
    for m in moves:
        board[m] = sign
        score = _minimax(board, opponent, sign)
        board[m] = None
        if score > best_score:
            best_score = score
            best_move = m
            # si score optimal trouvé, on sort
            if best_score == 1:
                break
    return best_move if best_move is not None else False
