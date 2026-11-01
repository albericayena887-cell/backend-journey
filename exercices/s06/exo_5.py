import csv
vll = ["nom", "prenom", "age"]


tetts = [{"nom": "DJINIMAKPOZO", "prenom": "Brigitte", "age" : 44}, {"nom": "AYENA", "prenom": "Judicael", "age" : 47}]
tett = {"nom" : "AYENA", "prenom" : "Roussel", "age" : 20}

with open("nex_c.csv", "w", encoding="utf-8", newline="") as file:
    fwrit = csv.DictWriter(file, fieldnames=vll ,delimiter=",")
    
    fwrit.writeheader()
    fwrit.writerow(tett)
    fwrit.writerows(tetts)




with open("nex_c.csv") as life:
    read = csv.DictReader(life, delimiter=",")

    for line in read:
        print(f" Le nom {line["nom"]} et le prénom {line["prenom"]}  ")
       