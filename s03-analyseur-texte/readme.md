# s03-analyseur-texte

Petit programme Python qui analyse un texte et affiche des statistiques sur ses mots.

## Ce que ça fait

Le programme lit un texte (en dur dans le script, ou depuis un fichier `.txt`) et affiche :

1. le **nombre de mots** ;
2. le **mot le plus long** et sa longueur ;
3. les **5 mots les plus fréquents** avec leur nombre d'apparitions ;
4. les **mots uniques** : le nombre de mots différents, et le nombre de mots qui n'apparaissent qu'une seule fois.

Avant l'analyse, le texte est mis en minuscules et la ponctuation (`, . ! ? ; :`) est remplacée par des espaces, pour que « Le » et « le », ou « chat, » et « chat », comptent comme le même mot.

Exemple de sortie avec le texte du script :

    Nombre de mots : 84
    Mot le plus long : considérablement ( 16 lettres )
    Top 5 :
       de : 4
       la : 3
       une : 3
       en : 3
       par : 3
    Mots différents : 65
    Mots qui n'apparaissent qu'une fois : 52

## Comment le lancer

Depuis le dossier du projet :

    python main.py

Si le texte est lu depuis un fichier, mets `exemple.txt` dans le même dossier que `main.py` et lance la commande depuis ce dossier (sinon Python lève une erreur `FileNotFoundError`).

## Choix que j'ai faits

- Les mots collés par une apostrophe ou un tiret (`l'esprit`, `serait-ce`) sont comptés comme **un seul mot**.
- Quand plusieurs mots sont à égalité pour la 5e place, je garde ceux que le tri place en premier.
- « Mots uniques » est donné de deux façons : les mots différents, et ceux vus une seule fois.

## Ce que j'ai appris
- **s03 :**
  - `=` : Affectation
  - `==` : Comparaison
  - `[::-1]` : Permet d'inverser une chaîne de caractères
  - `texte.split()` : découpe un texte en liste de mots ; `len(...)` d'une liste donne son nombre d'éléments
  - `len(texte)` compte les **caractères**, pas les mots
  - `texte.lower()` : passe le texte en minuscules ; `texte.replace(a, b)` : remplace un morceau de texte par un autre
  - `max(mots, key=len)` : trouve le mot le plus long
  - `set(...)` : garde uniquement les valeurs différentes (supprime les doublons)
  - dict : `compteur[mot] = compteur.get(mot, 0) + 1` pour compter des occurrences
  - `sorted(..., key=..., reverse=True)` et `[:5]` pour trier et garder les 5 premiers
  - `with open("fichier.txt", encoding="utf-8") as f:` pour lire un fichier

## Ce qui m'a bloqué
- **Compter les mots avec `len(texte)`** : ça donnait 551 (les caractères). Résolu en comptant les éléments de `texte.split()`, ce qui donne 84 mots.
- **Top 5 des mots fréquents** : ma première version parcourait les lettres au lieu des mots, et `max(texte.count(i))` plantait. Résolu en utilisant un dictionnaire de comptage, puis un tri.
- **L'ordre du nettoyage** : j'enlevais la ponctuation après avoir mesuré le plus long mot, donc les mots gardaient leur point. Résolu en nettoyant le texte une seule fois, au début.
- **Lire un fichier** : il faut le bon encodage (`utf-8`) et lancer le script depuis le dossier où se trouve le `.txt`.