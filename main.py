# Boucle de jeu (humain/IA), entrées clavier, lancement

# main.py
# --------
# Console game loop. Run this file to play.

from typing import Optional
from board import Board, print_board, check_winner, is_draw, make_move, available_moves
from ai import ia


def _human_turn(board: Board, sign: str) -> None:
    """
    Ask the human for a move (1..9), validate, and apply.
    Keep prompting until the move is legal.
    """
    while True:
        try:
            raw = input(f"Player {sign}, choose a cell (1-9): ").strip()
            idx = int(raw) - 1
            if make_move(board, idx, sign):
                return
            print("Illegal move, try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def _ai_turn(board: Board, sign: str) -> None:
    """
    Query the AI for a move via ia(board, sign) and play it.
    If ia() returns False unexpectedly, pick the first available move.
    """
    choice = ia(board, sign)
    if choice is False:
        moves = available_moves(board)
        if not moves:
            return
        choice = moves[0]
    make_move(board, int(choice), sign)
    print(f"AI ({sign}) plays at position {choice + 1}.")


def play_game(vs_ai: bool = True) -> None:
    """
    Main loop:
    - Start with empty board
    - X begins by convention
    - If vs_ai=True, O is the AI
    - After each move: print, check winner/draw, then switch
    """
    board: Board = [None] * 9
    current = 'X'
    print("Welcome to Tic Tac Toe!")
    print("Numbers (1..9) show free cells.\n")

    while True:
        print_board(board)

        if vs_ai and current == 'O':
            _ai_turn(board, current)
        else:
            _human_turn(board, current)

        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            return

        if is_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            return

        current = 'O' if current == 'X' else 'X'


if __name__ == "__main__":
    # Toggle to play human vs human: play_game(vs_ai=False)
    play_game(vs_ai=True)
