# ai.py — Intelligence Artificielle

Ce fichier fournit la fonction `ia(board, sign)` qui choisit un coup pour l'ordinateur.
Signature

- `ia(board: Board, sign: str) -> int | False`
  - Retourne un indice (0..8) si un coup est choisi, ou `False` si les entrées sont invalides ou si aucun coup n'est possible.
Stratégie (implémentation actuelle)

- Version minimale : IA basée sur l'algorithme Minimax (jeu optimal). L'IA évalue toutes les suites de coups et choisit l'action qui maximise ses chances.
Exemple d'utilisation

```python
Notes

- L'IA actuelle est déterministe (même position → même coup). Pour ajouter un mode "facile", on peut choisir aléatoirement parmi les meilleurs coups.
# README pour `ai.py`
# ai.py — Intelligence Artificielle

Ce fichier fournit la fonction `ia(board, sign)` qui choisit un coup pour l'ordinateur.

Signature

- `ia(board: Board, sign: str) -> int | False`
  - Retourne un indice (0..8) si un coup est choisi, ou `False` si les entrées sont invalides ou si aucun coup n'est possible.

Stratégie (implémentation actuelle)

- Version minimale : IA basée sur l'algorithme Minimax (jeu optimal). L'IA évalue toutes les suites de coups et choisit l'action qui maximise ses chances.

Exemple d'utilisation

```python
from board import new_board
# ai.py — Intelligence Artificielle

Ce fichier fournit la fonction `ia(board, sign)` qui choisit un coup pour l'ordinateur.

## Signature

- `ia(board: Board, sign: str) -> int | False`
  - Retourne un indice (0..8) si un coup est choisi, ou `False` si les entrées sont invalides ou s'il n'y a aucun coup possible.

## Stratégie (implémentation actuelle)

- L'IA utilise l'algorithme Minimax pour évaluer toutes les suites de coups et choisir un coup optimal (jeu parfait).

## Exemple d'utilisation

```python
from board import new_board
from ai import ia
b = new_board()
move = ia(b, 'O')
if move is not False:
    print('L IA joue en', move+1)
```

## Notes

- L'IA est déterministe (même position → même coup). Pour un mode "facile", on peut randomiser le choix parmi les meilleurs coups.
