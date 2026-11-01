# s06-csv-vers-json

Programme Python qui lit un fichier CSV de notes d'étudiants, calcule la moyenne de chacun, puis génère un fichier JSON et une page HTML de classement.

## Ce que ça fait

1. Lit `notes.csv` (colonnes : `nom`, `maths`, `python`, `anglais`).
2. Calcule la moyenne de chaque étudiant (arrondie à 2 décimales).
3. Ignore les lignes invalides en affichant un avertissement.
4. Écrit `resultats.json` (nom + moyenne).
5. Génère `classement.html` : un tableau trié de la meilleure à la plus faible moyenne.

`notes.csv` est le fichier d'entrée : il est lu, jamais modifié.

## Comment le lancer

Depuis le dossier du projet (celui qui contient `notes.csv`) :

    python main.py

Exemple de sortie :

    Ligne 9 ignorée : note invalide pour Pascal
    Ligne 10 ignorée : note invalide pour Julie
    Ligne 11 ignorée : nom manquant
    9 étudiants traités. Fichiers créés : resultats.json, classement.html

Ouvre ensuite `classement.html` dans ton navigateur (double-clic).

Si `notes.csv` n'existe pas :

    Erreur : le fichier notes.csv est introuvable.

## Fichiers du projet

    s06-csv-vers-json/
    ├── main.py            # le programme
    ├── notes.csv          # données d'entrée
    ├── resultats.json     # généré
    ├── classement.html    # généré
    └── README.md

## Choix que j'ai faits

- Une note doit être un nombre entre 0 et 20, sinon la ligne est ignorée.
- Une ligne sans nom, avec une note manquante ou non numérique est ignorée (avec un message et son numéro de ligne).
- La moyenne est enregistrée comme un **nombre** (`14.0`), pas comme un texte, pour pouvoir trier correctement.
- Les moyennes sont arrondies à 2 décimales.

## Ce que j'ai appris

### Lire et écrire des fichiers
- `with open("fichier.txt", encoding="utf-8") as f:` ouvre un fichier et le referme tout seul à la fin du bloc.
- Modes : `"r"` lecture (par défaut), `"w"` écriture (**écrase** le fichier).
- Toujours préciser `encoding="utf-8"` pour que les accents passent bien.
- `f.read()` lit tout, `f.write(texte)` écrit.
- Le fichier doit être trouvé depuis le dossier où on lance `python`, sinon `FileNotFoundError`.
- Règle : **l'entrée se lit, la sortie s'écrit dans d'autres fichiers** (on ne modifie pas `notes.csv`).

### Le format CSV
- Un CSV est un fichier texte : une ligne = un enregistrement, valeurs séparées par des virgules, première ligne = en-têtes.
- `csv.DictReader(f)` lit chaque ligne comme un dictionnaire : `ligne["nom"]`.
- Toutes les valeurs lues sont du **texte** : il faut convertir avec `float(...)` avant de calculer.
- Une valeur manquante donne `""` (deux virgules de suite) ou `None` (ligne trop courte).

### Le format JSON
- JSON est un format texte pour échanger des données : objets `{}`, listes `[]`, textes `"..."`, nombres, `true/false`, `null`.
- `json.dump(donnees, f, indent=4, ensure_ascii=False)` écrit dans un fichier (`indent` rend lisible, `ensure_ascii=False` garde les accents).
- `json.load(f)` relit un fichier JSON et redonne des listes et dictionnaires Python.
- Équivalents Python : objet → `dict`, liste → `list`, `null` → `None`.
- Garder les nombres comme nombres (`14.0`), pas comme textes (`"14.0"`).

### Générer une page HTML
- Un tableau HTML : `<table>`, `<tr>` (ligne), `<th>` (titre de colonne), `<td>` (case).
- Je construis les lignes avec une boucle et une f-string, puis je mets le tout dans un modèle de page (chaîne entre triples guillemets).
- `<meta charset="utf-8">` pour que les accents s'affichent bien.

### Trier et classer
- `sorted(liste, key=lambda e: e["moyenne"], reverse=True)` trie du plus grand au plus petit.
- `enumerate(liste, start=1)` donne le rang en même temps que l'élément.
- On ne peut trier correctement que des **nombres** (le texte `"9.0"` passe avant `"18.0"`).

### Gérer les erreurs
- `try / except FileNotFoundError` : fichier absent → message clair au lieu d'un plantage.
- `try / except (TypeError, ValueError)` : `float("abc")` et `float(None)` plantent, on les attrape pour ignorer la ligne.
- `continue` saute au tour suivant de la boucle.
- Afficher un message précis (numéro de ligne + nom) pour savoir pourquoi une ligne est ignorée.

### Organisation du code
- Une fonction = un rôle : `lire_etudiants`, `ecrire_json`, `ecrire_html`, `main`.
- `if __name__ == "__main__": main()` lance le programme seulement quand on exécute le fichier directement.
- Constantes en majuscules en haut du fichier (`FICHIER_CSV`, `MATIERES`) pour éviter de répéter les valeurs.

## Ce qui m'a bloqué

- **La moyenne en texte** : j'avais fait `str(moyenne)`, donc le JSON contenait `"14.0"`. Impossible de trier correctement ensuite. Résolu en gardant un nombre.
- **L'écriture dans la boucle** : mon `open(..., "w")` était dans le `for`, donc le fichier était réécrit à chaque étudiant. Résolu en l'écrivant une seule fois, après la boucle.
- **Les trois `isdigit`** : ils rejettent les nombres négatifs, plantent sur `None`, et `isalpha()` refusait les noms avec un tiret ou un espace. Résolu avec `float(...)` dans un `try / except`.
- **Ne pas modifier `notes.csv`** : j'avais cru qu'il fallait le transformer. En réalité on lit l'entrée et on écrit les résultats dans de nouveaux fichiers.
- ... (à compléter avec ce qui t'a vraiment bloqué)