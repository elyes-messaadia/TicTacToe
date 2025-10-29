# Boucle de jeu (humain/IA), entrées clavier, lancement

# main.py
# --------
# Console game loop. Run this file to play.

from typing import Optional
from board import Board, print_board, check_winner, is_draw, make_move, available_moves
from ai import ia


def get_human_move(board: Board, sign: str) -> int:
    """Demande au joueur humain un index valide (0..8) et le retourne."""
    while True:
        raw = input(f"Joueur {sign}, choisissez une case (1-9) : ").strip()
        if not raw.isdigit():
            print("Entrez un nombre entre 1 et 9.")
            continue
        idx = int(raw) - 1
        if make_move(board, idx, sign):
            return idx
        print("Coup invalide, réessayez.")


def play_game(vs_ai: bool = True) -> None:
    """Boucle principale du jeu (humain vs humain ou humain vs IA).

    - X commence
    - si vs_ai=True alors O est l'IA
    """
    board: Board = [None] * 9
    current = "X"
    print("Bienvenue au Tic Tac Toe !")
    print("Les chiffres (1..9) indiquent les cases libres.\n")

    while True:
        print_board(board)

        if vs_ai and current == "O":
            choice = ia(board, current)
            if choice is False:
                moves = available_moves(board)
                if not moves:
                    print("Aucun coup possible.")
                    return
                choice = moves[0]
            make_move(board, int(choice), current)
            print(f"IA ({current}) joue en position {choice + 1}.")
        else:
            get_human_move(board, current)

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Le joueur {winner} a gagné ! 🎉")
            return

        if is_draw(board):
            print_board(board)
            print("Match nul ! 🤝")
            return

        current = "O" if current == "X" else "X"


if __name__ == "__main__":
    play_game(vs_ai=True)
