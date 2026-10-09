# dict = key + value

dic = {
    "name" : "John",
    "Age" : 18,
    "cars" : ["ferrari", "mercedes", "aston martin", "BMW", "Rolls Royce"]

}
for key, value in dic.items():
    print(key, value)

#age = dic.pop("Age") # il enlève le key Age et assigne sa valeur à age . On peut meme le print . Il agit automatiquement sur le dic
#print(dic)
#print(age)
#print(dic.keys()) #pour avoir toutes les clés du dic

"""
#(dic.get("name"))
print(dic["name"])   #John  ou encore 
print(dic["cars"])   #['ferrari', 'mercedes', 'aston martin', 'BMW', 'Rolls Royce']
print(dic["Age"])    #18


# Non existing key
print(dic.get("phone", "N'existe pas parceque phone n'est pas une clé existante")) #N'existe pas parceque phone n'est pas une clé existante

"""