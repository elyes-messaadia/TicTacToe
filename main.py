"""Boucle console pour jouer au Tic Tac Toe.

Fichiers utilitaires : `board.py` (plateau/règles) et `ai.py` (IA).
Les docstrings ci-dessous expliquent chaque fonction pour faciliter la compréhension.
"""
from typing import Optional
from board import new_board, print_board, make_move, check_winner, is_draw, available_moves
from ai import ia


def get_human_move(board: list, sign: str) -> int:
    """Demande à l'utilisateur une case (1..9), l'applique et retourne l'indice joué."""
    while True:
        s = input(f"Joueur {sign}, choisissez une case (1-9) : ").strip()
        if not s.isdigit():
            print("Entrez un numéro entre 1 et 9.")
            continue
        idx = int(s) - 1
        if make_move(board, idx, sign):
            return idx
        print("Coup invalide ou case occupée.")


def play_game(vs_ai: bool = True) -> None:
    """Joue une partie complète.

    vs_ai True : l'IA joue les 'O'.
    La boucle affiche le plateau, demande ou calcule un coup, teste victoire/nul.
    """
    board = new_board()
    current = 'X'
    ai_sign = 'O' if vs_ai else None
    print("Bienvenue au Tic Tac Toe !")
    while True:
        print_board(board)
        if vs_ai and current == ai_sign:
            move = ia(board, current)
            if move is False:
                movs = available_moves(board)
                if not movs:
                    print("Aucun coup possible.")
                    return
                move = movs[0]
            make_move(board, int(move), current)
            print(f"IA ({current}) joue en {move+1}.")
        else:
            get_human_move(board, current)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Le joueur {winner} a gagné !")
            return
        if is_draw(board):
            print_board(board)
            print("Match nul !")
            return
        current = 'O' if current == 'X' else 'X'


if __name__ == '__main__':
    play_game(vs_ai=True)

