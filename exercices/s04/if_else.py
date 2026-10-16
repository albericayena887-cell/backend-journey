#is : c'est pour determiner si les deux variables ont la meme adresse mémoire
# a = [1, 2, 3]               ||
# b = [1, 2, 3]               || b = a
# print( a == b ) : True      ||  True
# print( a is b ) : False     ||  True


user = "Admin"
logged_in = False

if not logged_in:
    print("Acces refused")
else:
    print("Access granted")    