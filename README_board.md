# board.py — Plateau et règles

`board.py` contient la logique du plateau et des règles du jeu.

Fonctions principales :

- `new_board()` -> crée et retourne un plateau vide (liste de 9 `None`).
- `print_board(board)` -> affiche le plateau en 3x3 ; les cases vides affichent leur numéro (1..9).
- `available_moves(board)` -> liste des indices libres (0..8).
- `make_move(board, index, sign)` -> applique un coup si valide (`'X'` ou `'O'`) et retourne `True`/`False`.
- `check_winner(board)` -> retourne `'X'` ou `'O'` si un joueur a gagné, sinon `None`.
- `is_draw(board)` -> `True` si le plateau est plein sans gagnant.

Exemple rapide :

```python
from board import new_board, make_move, print_board
b = new_board()
make_move(b, 0, 'X')
print_board(b)
```

Remarque : `make_move` modifie le plateau en place.
