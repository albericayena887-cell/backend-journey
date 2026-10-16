def describe_pet(pet_name, animal_type='dog'):
    # On combine les deux phrases avec \n pour le saut de ligne
    return f"I have a {animal_type}.\nMy {animal_type}'s name is {pet_name.title()}."

# On stocke le résultat dans une variable, puis on l'affiche
info_animal = describe_pet(pet_name='willie')
print(info_animal)
