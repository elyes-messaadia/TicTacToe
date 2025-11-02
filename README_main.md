# main.py — Boucle de jeu (console)

Ce fichier contient la boucle principale pour jouer en console.

Fonctions principales :

- `get_human_move(board, sign)` : lit la saisie de l'utilisateur (1..9), valide et applique le coup (retourne l'indice 0..8).
- `play_game(vs_ai=True)` : lance une partie complète ; si `vs_ai=True`, l'IA joue les 'O'.

Entrées / sorties :

- Entrées : saisies clavier du joueur (1..9).
- Sorties : affichage du plateau et messages de progression/fin.

Exemple d'utilisation :

```powershell
python main.py
```

Astuce : pour jouer humain vs humain, appeler `play_game(vs_ai=False)`.
