#{'TEEO', 'maths', 'Histoire', 'Anglais'}, {'Histoire', 'Anglais', 'maths', 'TEEO'}   A chaque print , il change tout le temps

cs_course = {"maths", "Histoire", "Anglais", "TEEO"}
art_course = {"espagnole", "Histoire", "Art", "TEEO"}
print(cs_course.intersection(art_course))  
print(cs_course.difference(art_course))
print(cs_course.union(art_course))
#pour créer un set vide , on a set() ; pas {} , cela est pour le dictionnaire