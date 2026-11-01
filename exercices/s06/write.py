with open("example.txt", "w") as file:
    file.write("Hello, world!\n")

with open("example.txt", "a") as file:
    file.write("Hello i'm Roussel")    


# Si le fichier n'existais pas , il le crée dans le meme répertoire
# le "w" ecrase ce qu'il y a avit dans le le fichier , donc , si on veut ajouter un truc , c'est mieux d'utimiser "a" 