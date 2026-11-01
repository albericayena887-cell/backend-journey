import csv
import json

FICHIER_CSV = "notes.csv"
FICHIER_JSON = "resultats.json"
FICHIER_HTML = "classement.html"
MATIERES = ["maths", "python", "anglais"]


def lire_etudiants(chemin):
    """Lit le CSV, calcule les moyennes, ignore les lignes invalides."""
    etudiants = []
    with open(chemin, encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for numero, ligne in enumerate(lecteur, start=2):
            nom = (ligne.get("nom") or "").strip()
            if not nom:
                print(f"Ligne {numero} ignorée : nom manquant")
                continue
            try:
                notes = [float(ligne[m]) for m in MATIERES]
            except (TypeError, ValueError):
                print(f"Ligne {numero} ignorée : note invalide pour {nom}")
                continue
            if any(n < 0 or n > 20 for n in notes):
                print(f"Ligne {numero} ignorée : note hors de 0 à 20 pour {nom}")
                continue
            moyenne = round(sum(notes) / len(notes), 2)
            etudiants.append({"nom": nom, "moyenne": moyenne})
    return etudiants


def ecrire_json(etudiants, chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(etudiants, f, indent=4, ensure_ascii=False)


def ecrire_html(chemin_json, chemin_html):
    with open(chemin_json, encoding="utf-8") as f:
        etudiants = json.load(f)
    classement = sorted(etudiants, key=lambda e: e["moyenne"], reverse=True)

    lignes = ""
    for rang, e in enumerate(classement, start=1):
        lignes += f"    <tr><td>{rang}</td><td>{e['nom']}</td><td>{e['moyenne']:.2f}</td></tr>\n"

    page = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Classement</title>
</head>
<body>
  <h1>Classement</h1>
  <table border="1" cellpadding="6">
    <tr><th>Rang</th><th>Nom</th><th>Moyenne</th></tr>
{lignes}  </table>
</body>
</html>
"""
    with open(chemin_html, "w", encoding="utf-8") as f:
        f.write(page)


def main():
    try:
        etudiants = lire_etudiants(FICHIER_CSV)
    except FileNotFoundError:
        print(f"Erreur : le fichier {FICHIER_CSV} est introuvable.")
        return
    ecrire_json(etudiants, FICHIER_JSON)
    ecrire_html(FICHIER_JSON, FICHIER_HTML)
    print(f"{len(etudiants)} étudiants traités. Fichiers créés : {FICHIER_JSON}, {FICHIER_HTML}")


if __name__ == "__main__":
    main()