def palindrome(mot):
    if mot[::-1] == mot:
        return True
    else:
        return False

mot = input("Entrez votre mot: ").replace(" ", "").lower()    
resultat = palindrome(mot) 
print(resultat)