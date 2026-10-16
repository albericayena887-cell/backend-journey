def presenter_identite(*args, **kwargs):
    print(kwargs)   # {'nom': 'Alice', 'age': 25}
    print(args)     # ('age', 12, 15.5)

presenter_identite("age", 12, 15.5, nom="Alice", age=25)

