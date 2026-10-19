from utils import NIVEAUX, demander_niveau, choisir_nombre

niveau = demander_niveau()
nombre_secret = choisir_nombre(niveau)
essais_max = NIVEAUX[niveau]["essais"]

print(f"J'ai choisi un nombre entre 1 et {NIVEAUX[niveau]['max']}. Tu as {essais_max} essais.")