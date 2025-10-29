README pour `main.py`

But: TicTacToe - boucle de jeu

But: Contenu

- `get_human_move(board, sign)` : demande et applique un coup humain valide (1..9). Retourne l'index joué.
- `play_game(vs_ai=True)` : boucle principale. Si `vs_ai` est True, l'IA joue les 'O'. Le jeu alterne X/O, affiche le plateau, détecte victoire/nul et affiche le résultat.

Entrées / sorties

- Entrées : saisies clavier du joueur (1..9) lors du tour humain.
- Sorties : affichage console du plateau et messages de fin.

Exemple d'utilisation

Lancer le jeu :

```powershell
python main.py
```

Conseils

- Pour jouer humain vs humain, appeler `play_game(vs_ai=False)`.
- Les messages sont en français pour faciliter la prise en main.
