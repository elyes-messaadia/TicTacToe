README pour `ai.py`

Rôle

`ai.py` fournit la fonction `ia(board, sign)` utilisée pour décider d'un coup pour l'IA.

Signature

- `ia(board: Board, sign: str) -> int | False`
  - Retourne un indice (0..8) si un coup est choisi, ou `False` en cas d'entrée invalide ou si aucun coup n'est possible.

Stratégie

1. Gagner immédiatement si possible.
2. Bloquer le coup gagnant de l'adversaire.
3. Prendre le centre si libre.
4. Prendre un coin libre.
5. Prendre un côté.

Exemple

```python
from board import Board
from ai import ia
b: Board = [None]*9
move = ia(b, 'O')
if move is not False:
    print('L IA joue', move+1)
```

Notes

- La fonction effectue des vérifications simples sur les entrées et renvoie `False` si elles sont invalides.
- Le code est déterministe (même situation -> même coup).
