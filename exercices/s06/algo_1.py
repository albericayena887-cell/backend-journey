def dict(lev): 
    dico_freq = {}  

    for mom in lev:
        dico_freq[mom] = dico_freq.get(mom, 0) + 1
    return dico_freq 


lev = input("Entrez une phrase: ").lower().split()
resultat = dict(lev)
print(resultat)