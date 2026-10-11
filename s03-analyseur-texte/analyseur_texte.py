texte = """La lecture quotidienne est une habitude simple mais extrêmement bénéfique pour l'esprit. En effet, ... général."""

# 0- Nettoyage : une seule fois, au début
for p in ",.!?;:":
    texte = texte.replace(p, " ")
mots = texte.lower().split()

# 1- Le nombre de mots
print("Nombre de mots :", len(mots))

# 2- Le plus long mot
plus_long = ""
for mot in mots:
    if len(mot) > len(plus_long):
        plus_long = mot
print("Mot le plus long :", plus_long, "(", len(plus_long), "lettres )")

# 3- Les 5 mots les plus fréquents
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

classement = sorted(compteur.items(), key=lambda paire: paire[1], reverse=True)
print("Top 5 :")
for mot, nb in classement[:5]:
    print("  ", mot, ":", nb)

# 4- Les mots uniques
mots_differents = set(mots)
print("Mots différents :", len(mots_differents))

apparait_une_fois = [mot for mot, nb in compteur.items() if nb == 1]
print("Mots qui n'apparaissent qu'une fois :", len(apparait_une_fois))