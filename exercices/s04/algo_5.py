# Initialisation des variables (tu peux changer ces valeurs)
a = 12
b = 18

# Copie des valeurs d'origine pour l'affichage final
original_a = a
original_b = b

# Algorithme d'Euclide
while b != 0:
    a, b = b, a % b

# Affichage du résultat
print(f"Le PGCD de {original_a} et {original_b} est : {a}")
