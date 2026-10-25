def est_palindrome(texte):
    """True si le texte se lit pareil dans les deux sens.
    On ignore les majuscules et les espaces."""
    propre = texte.lower().replace(" ", "")
    return propre == propre[::-1]


def nettoyer(liste):
    """Enlève les espaces autour, met en minuscules, supprime les éléments vides."""
    return [t.strip().lower() for t in liste if t.strip() != ""]


def trier_personnes(personnes):
    """Trie des (nom, age) par âge croissant, puis par nom à âge égal."""
    return sorted(personnes, key=lambda p: (p[1], p[0]))


def afficher_tableau(personnes):
    """Affiche les personnes en colonnes alignées."""
    print(f"{'Nom':<10}{'Âge':>5}")
    print("-" * 15)
    for nom, age in personnes:
        print(f"{nom:<10}{age:>5}")