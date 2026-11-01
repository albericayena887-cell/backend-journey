import json

with open("jjs.json", "r", encoding="utf-8") as lic:
    vlac = json.load(lic)

vlac["nom"] = "AYENA"
vlac["adresse"]["ville"] = "cotonou"
vlac["competences"].append("PHP")

with open("jjs.json", "w", encoding="utf-8") as lic:
        json.dump(vlac, lic, indent=4)
