def rense(name, age):
    
    if age == 20:
        age += 1
    else:
        age *= 2    
    
    return {"NAME" : name, "AGE" : age}
name  = input("Enter your name: ")
age = int(input("Enter your age: "))
cor = rense(name, age)
print(cor)