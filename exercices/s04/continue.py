panier = ["pomme", "banane", "brocoli", "orange", "carotte"]

for aliment in panier:
    if aliment == "brocoli" or aliment == "carotte":
        continue  # ⏭️ On passe directement à l'aliment suivant !
    
    print("J'adore ce fruit :", aliment)
