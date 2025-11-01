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
	La fonction simule chaque coup disponible, appelle récursivement
	_minimax pour évaluer la position résultante, puis restaure la case.
	"""
	winner = check_winner(board)
	# Cas terminals : victoire de l'une des deux équipes
	if winner == ai_sign:
		return 1
	if winner is not None:
		return -1
	moves = available_moves(board)
	# Aucun coup possible => match nul
	if not moves:
		return 0

	# Si c'est au tour de l'IA, on maximise le score
	if player == ai_sign:
		best = -2
		for m in moves:
			# Simule le coup
			board[m] = player
			score = _minimax(board, 'O' if player == 'X' else 'X', ai_sign)
			# Restaure la case
			board[m] = None
			# Garde le meilleur score (max)
			if score > best:
				best = score
				# Coup gagnant : on peut arrêter la recherche
				if best == 1:
					break
		return best
	# Sinon c'est le tour de l'adversaire : on minimise
	else:
		worst = 2
		for m in moves:
			board[m] = player
			score = _minimax(board, 'O' if player == 'X' else 'X', ai_sign)
			board[m] = None
			if score < worst:
				worst = score
				# Coup assurant la défaite pour l'IA : prune
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
		# Simule le coup, évalue la position, puis restaure
		board[m] = sign
		score = _minimax(board, 'O' if sign == 'X' else 'X', sign)
		board[m] = None
		# Choisit le coup qui maximise le score pour l'IA
		if score > best_score:
			best_score = score
			best_move = m
			# Si on trouve un coup gagnant on peut sortir tôt
			if best_score == 1:
				break
	# Si aucun coup trouvé (improbable), retourne False
	return best_move if best_move is not None else False
