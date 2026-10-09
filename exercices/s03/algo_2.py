name = input("Entrez un mot: ")  # On retire .split()

voyelles = ["a", "e", "u", "o", "A", "E", "I", "O", "U", "i"]
compteur = 0

for lettre in name:
    if lettre in voyelles:
        compteur += 1

print("Nombre de voyelles :", compteur)