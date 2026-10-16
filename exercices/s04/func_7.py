def greet(name, age=20):
    print(f"I am {name} and i have {age} years old! ")

name = input("Enter your name: ")
age = int(input("Ton age: "))     # on aurait pu faire ça et écrire une autre valeur si on ajoute 
greet(name)                       # ça en bas (name, age) ou (name, age=20) 