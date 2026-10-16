"""
name = ""
while name != "Sesame":
    name = input("Entrez le mot magique: ")
    if name != "Sesame":                                  #UNE autre façon de voir les choses
        print("Recommence encore ")

print("Succès!!!!")
print("La porte s'ouvre")



"""

while True:
    name = input("Entrez le mot magique: ")

    if name != "Sesame":
        print("Recommence encore ")
    else:
        print("Succès!!!!")
        print("La porte s'ouvre")
        break  