nb = int(input("Entrez le nombre: "))
rae = list(range(1, nb+1))
rl = []
#print(rae)
for ni in rae:
    if (ni%3 == 0 and ni%5 == 0):
        rl.append("FizzBuzz")
    elif  ni%5 == 0:
        rl.append("Buzz")
    elif ni%3 == 0:
        rl.append("Fizz")    
    else:
        rl.append(str(ni))     
print(rl)    