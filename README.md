# TicTacToe

Petit jeu Tic-tac-toe en console (Python).

Ce dépôt contient une implémentation simple du jeu avec :

- `main.py` : boucle de jeu et interactions utilisateur (console).
- `board.py` : représentation du plateau et règles du jeu.
- `ai.py` : intelligence artificielle (minimax) pour jouer contre l'ordinateur.

## Lancer le jeu

Ouvrir un terminal dans le dossier du projet et exécuter :

```powershell
python main.py
```

Le jeu démarre en mode humain vs IA (X = humain, O = IA). Pour jouer humain vs humain, ouvrez `main.py` et appelez `play_game(vs_ai=False)`.

## Fichiers principaux

- `board.py` : fonctions pour créer et afficher un plateau, tester gagnant/nul, appliquer un coup.
- `ai.py` : IA utilisant minimax pour choisir un coup optimal.
- `main.py` : boucle de jeu, lecture des entrées et affichage.

## Prochaines étapes possibles

- Ajouter des tests unitaires pour `board.py` et `ai.py`.
- Ajouter un mode de difficulté (randomiser les coups de l'IA pour un niveau facile).
- Ajouter une interface graphique légère (Tkinter/PySimpleGUI).

Voir les fichiers `README_board.md`, `README_ai.md` et `README_main.md` pour des détails par module.

