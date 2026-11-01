import csv


with open("names.csv", encoding="utf-8") as life:
    vvs = csv.DictReader(life, delimiter=",")
    for lil in vvs:
        print(lil)
        #print(f"Son prénom {lil['first_name']}, son nom {lil['last_name']} et son mail {lil['email']}")