import json
Donnees = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 34,
    "est_actif": True,
    "competences": ["Python", "HTML", "SQL"],

    "adresse": {
        "ville": "Paris",
        "code_postal": "75001"
    }
}
with open("jjs.json", "w", encoding="utf-8") as fichier:
    json.dump(Donnees, fichier, indent=4, ensure_ascii=False)