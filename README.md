# TicTacToe

Petit jeu Tic Tac Toe en console.

Fichiers importants :

- `main.py` : boucle de jeu et interactions utilisateur.
- `board.py` : logique du plateau et règles.
- `ai.py` : IA simple et déterministe.

Pour jouer :

```powershell
python main.py
```

Voir les fichiers `README_*.md` pour des explications détaillées par module.

# Tic Tac Toe — Python (Console + IA)

Version console du classique **Tic Tac Toe** avec une **Intelligence Artificielle** simple et explicable.  
Les **commentaires dans le code sont en anglais** pour t’aider à présenter précisément le rôle de chaque fonction.

---

## 🎯 Objectifs

- Implémenter les **règles du jeu** (gagnant, nul, coups légaux).  
- Coder une **IA** conforme à la signature imposée : `def ia(board, signe) -> int | False`.  
- Structurer le code en **trois fichiers** clairs et réutilisables.  
- (Optionnel) Préparer une **interface graphique** (Tkinter) sans toucher à la logique.

---

## 🗂️ Structure du dépôt

tictactoe/
├─ board.py # Plateau + règles (gagnant, nul, coups dispo, appliquer un coup, affichage)
├─ ai.py # Fonction ia(board, signe) + helper interne
└─ main.py # Boucle de jeu console (humain/IA), entrées clavier, exécutable principal

### Détails par fichier

**`board.py` — Règles & plateau**

- Représentation : liste de 9 cases (`['X', 'O', None]`), indices 0..8.
- `WIN_LINES` : toutes les combinaisons gagnantes.
- Fonctions :  
  - `print_board(board)` — affiche une grille lisible (1..9 pour viser les cases vides).  
  - `check_winner(board) -> Optional[str]` — renvoie `'X'`, `'O'` ou `None`.  
  - `is_draw(board) -> bool` — plateau plein sans gagnant.  
  - `available_moves(board) -> List[int]` — indices libres.  
  - `make_move(board, index, sign) -> bool` — applique un coup si légal.

**`ai.py` — Intelligence Artificielle**

- Signature exigée : `ia(board, signe) -> int | False`.
- Validations d’entrée (types/valeurs).
- Stratégie déterministe, facile à expliquer :  
  1) Gagner tout de suite.  
  2) Bloquer une victoire adverse immédiate.  
  3) Prendre le **centre** (4).  
  4) Prendre un **coin** (0,2,6,8).  
  5) Prendre un **côté** (1,3,5,7).  
- Retourne un **indice 0..8** ou **`False`** (erreur / aucun coup).

**`main.py` — Boucle de jeu (console)**

- Point d’entrée.  
- Par défaut : **X = humain**, **O = IA**.  
- `play_game(vs_ai=True)` ; passer `False` pour **humain vs humain**.  
- Alterne les tours → affiche → vérifie gagnant/nul → termine proprement.

---

## ▶️ Lancer le projet

1. Ouvre un terminal dans le dossier `tictactoe/`.  
2. Exécute :

```bash
python main.py
