while True:
    nb = int(input("Entrez le nombre secret: "))
    if nb < 42:
        print("C'est plus")        
    elif nb > 42:
        print("C'est lent")
    else:
        print("Bravo !")
        break    