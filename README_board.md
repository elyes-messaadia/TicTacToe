README pour `board.py`

But: Rôle

`board.py` contient la représentation du plateau et les règles de base :

- Type `Board` : liste de 9 éléments (None, 'X', 'O').
- `print_board(board)` : affiche le plateau en 3x3. Les cases vides sont numérotées 1..9.
- `check_winner(board)` : retourne 'X' ou 'O' si l'un a gagné, sinon None.
- `is_draw(board)` : vrai si toutes les cases sont occupées et qu'il n'y a pas de gagnant.
- `available_moves(board)` : liste des indices libres (0..8).
- `make_move(board, index, sign)` : essaye de jouer; retourne True si coup valide et appliqué.

Exemples rapides

```python
from board import Board, print_board, make_move
b: Board = [None]*9
make_move(b, 0, 'X')
print_board(b)
```

Notes

- Toutes les fonctions sont pures sur la logique du jeu sauf `make_move` qui modifie le plateau.
