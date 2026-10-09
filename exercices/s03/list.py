"""
print(sum(cars)) : pour faire la somme
sort(reverse=False): pour ordonner la liste
sorted(cars): marche bien

reverse() ou sort(reverse=True): pour mettre à l'envers la liste 
"""

cars = ["honda", "toyota", "ferrari", "chevrolet", "Aston martin", "Range rover"]

cars_2 = ["ford", "mercedes", "lambo", "BMW"]

#cars_2.pop()
#print(cars_2) # ['ford', 'mercedes', 'lambo']

#new = cars_2.pop()
#print(new) # Quand on lui assigne une valeur , lambo

#print(cars[1:5]) # ['toyota', 'ferrari', 'chevrolet', 'Aston martin']

cars_2.extend(cars)
print(cars_2) #['ford', 'mercedes', 'lambo', 'BMW', 'honda', 'toyota', 'ferrari', 'chevrolet', 'Aston martin', 'Range rover'] , pas de append
cars_2.sort(reverse=True)
print(cars_2) #['toyota', 'mercedes', 'lambo', 'honda', 'ford', 'ferrari', 'chevrolet', 'Range rover', 'BMW', 'Aston martin']
#pour créer une liste  vide , on a list() et  [] 
