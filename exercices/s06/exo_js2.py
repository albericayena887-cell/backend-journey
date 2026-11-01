import json

with open("jjs.json", "r") as fich:
    donne = json.load(fich)

    #print(donne)
    print(donne["nom"])
    print(donne["adresse"])
    print(donne["adresse"]["ville"])
