# Saisie de l'entier n
n = int(input("Entrez un nombre: "))

# Cas de base
if n < 2:
  print(False)
else:
  est_premier = True
  i = 2

  # Équivaut à tester jusqu'à la racine carrée de n
  while i * i <= n:
    if n % i == 0:
      est_premier = False
      break
    i += 1  # On passe au diviseur suivant

  print(est_premier)
