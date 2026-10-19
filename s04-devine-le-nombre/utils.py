import random

NIVEAUX = {
    "facile":    {"max": 10,  "essais": 5},
    "moyen":     {"max": 50,  "essais": 7},
    "difficile": {"max": 100, "essais": 7},
}


def demander_niveau():
    """Redemande tant que le niveau n'est pas valide, puis le renvoie."""
    while True:
        niveau = input("Niveau (facile / moyen / difficile) : ").lower().strip()
        if niveau in NIVEAUX:
            return niveau
        print("Niveau invalide, réessaie.")


def choisir_nombre(niveau):
    """Renvoie un nombre secret entre 1 et la borne du niveau."""
    return random.randint(1, NIVEAUX[niveau]["max"])