# Carnet d'erreurs

Pour chaque erreur : le message, la cause, la correction, et ce que j'en retiens.
Les plus récentes sont en haut.

---

## S3 · TypeError: can only concatenate str (not "int") to str
- **Contexte :** exercice sur les chaînes (Corey 2)
- **Code :** `print("J'ai " + 20 + " ans")`
- **Cause :** on ne peut pas coller une chaîne et un entier avec `+`.
- **Correction :** `print(f"J'ai {20} ans")` ou `print("J'ai " + str(20) + " ans")`
- **À retenir :** utiliser les f-strings pour mélanger texte et nombres.

## S2 · fatal: not a git repository
- **Contexte :** commande `git status` lancée hors du dépôt
- **Cause :** je n'étais pas dans le dossier `backend-journey`.
- **Correction :** `cd` jusqu'au dossier du dépôt, puis relancer.
- **À retenir :** vérifier le dossier courant avec `pwd` (ou `ls`) avant une commande Git.

## S1 · Permission denied
- **Contexte :** lancer mon script `rapport_logs.sh`
- **Cause :** le fichier n'avait pas le droit d'être exécuté.
- **Correction :** `chmod +x rapport_logs.sh`
- **À retenir :** un script a besoin du droit `x` pour s'exécuter directement.
