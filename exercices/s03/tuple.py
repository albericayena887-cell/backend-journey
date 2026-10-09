# MUTABLE
## j'ai juste modifié la "copie" et l'original a été aussi modifié . 
## Voilà de quoi on parle quand on dit mutable. Ils ont la meme addresse mémoir
"""
list = ["cotonou", "tokyo", "Durban", "paris", "seattle"]
list_2 = list
print(list)   #['cotonou', 'tokyo', 'Durban', 'paris', 'seattle']
print(list_2) #['cotonou', 'tokyo', 'Durban', 'paris', 'seattle'] clean 

list_2[0] = "washington"

print(list)    #['washington', 'tokyo', 'Durban', 'paris', 'seattle']
print(list_2)  #['washington', 'tokyo', 'Durban', 'paris', 'seattle']
"""
#IMMUTABLE

list = ("cotonou", "tokyo", "Durban", "paris", "seattle")
list_2 = list
print(list)   #['cotonou', 'tokyo', 'Durban', 'paris', 'seattle']
print(list_2) #['cotonou', 'tokyo', 'Durban', 'paris', 'seattle'] clean 

list_2[0] = "washington"

print(list)    #['washington', 'tokyo', 'Durban', 'paris', 'seattle']
print(list_2)  #['washington', 'tokyo', 'Durban', 'paris', 'seattle']

# ici pas d'ajout et de remove , c'est un peu limité
#pour créer un tuple vide , on a tuple() et  () 