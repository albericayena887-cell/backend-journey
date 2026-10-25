iss = [1, 2, 3, 4, 6, 7, 9]
lm = []

lm = [n*n for n in iss]   # i want n*n for n in d
ll = [n for n in iss if n%2 == 0]
ln = list(filter(lambda n: n%2 == 0, iss ))
"""
for n in iss:
    lm.append(n)
"""
print (lm)    
print (ll)    
print (ln)