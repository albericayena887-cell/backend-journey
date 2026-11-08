try:
    resultat = 1 / 0
except Exception as e:
    # 1. Pour afficher le type de l'erreur (ex: <class 'ZeroDivisionError'>)
    print("Type de l'erreur :", type(e))
    
    # 2. Pour obtenir uniquement le nom propre de l'erreur (ex: ZeroDivisionError)
    print("Nom de l'erreur :", type(e).__name__)
    
    # 3. Pour afficher le message explicatif (ex: division by zero)
    print("Message de l'erreur :", e)
