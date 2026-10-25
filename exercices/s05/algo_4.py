def sans_doublons(liste):
    resultat = []
    for element in liste:
        if element not in resultat:
            resultat.append(element)
    return resultat

liste = [2, 3, 2, 5, 5, 6]
print (sans_doublons(liste))
