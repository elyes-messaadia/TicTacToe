"""IA pour Tic Tac Toe.

Fonction principale : ia(board, sign) -> int|False.
Retourne l'indice (0..8) du meilleur coup via minimax simple (explorable) ou False
si les entrées sont invalides ou s'il n'y a pas de coup.
"""
from typing import List, Optional, Union
from board import Board, available_moves, check_winner


def _minimax(board: Board, player: str, ai_sign: str) -> int:
	"""Minimax renvoyant le score depuis la position courante pour ai_sign.

	Scores : +1 si ai_sign gagne, -1 si perd, 0 pour nul.
	Cette fonction modifie temporairement le plateau puis restaure la case.
	"""
	winner = check_winner(board)
	if winner == ai_sign:
		return 1
	if winner is not None:
		return -1
	moves = available_moves(board)
	if not moves:
		return 0

	# maximiser si c'est au tour de l'IA
	if player == ai_sign:
		best = -2
		for m in moves:
			board[m] = player
			score = _minimax(board, 'O' if player == 'X' else 'X', ai_sign)
			board[m] = None
			if score > best:
				best = score
				if best == 1:
					break
		return best
	else:
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
	"""Choisit un coup pour `sign`.

	Validation minimale des entrées. Renvoie False si invalide ou pas de coups.
	Utilise minimax pour choisir le meilleur coup (jeu optimal).
	"""
	if sign not in ("X", "O") or not isinstance(board, list) or len(board) != 9:
		return False
	if any(cell not in (None, "X", "O") for cell in board):
		return False

	moves = available_moves(board)
	if not moves:
		return False

	best_move: Optional[int] = None
	best_score = -2
	for m in moves:
		board[m] = sign
		score = _minimax(board, 'O' if sign == 'X' else 'X', sign)
		board[m] = None
		if score > best_score:
			best_score = score
			best_move = m
			if best_score == 1:
				break
	return best_move if best_move is not None else False
