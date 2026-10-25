def deuxieme_plus_grand(l):

    last = sorted(set(l))
    
    if len(last) >= 2:
        return last[-2]
    else:
        return None



print(deuxieme_plus_grand([4, 9, 2, 9]))
print(deuxieme_plus_grand([5, 5]))
print(deuxieme_plus_grand([1, 2]))  