from outils import est_palindrome, nettoyer, trier_personnes

assert est_palindrome("radar") is True
assert est_palindrome("Kayak") is True
assert est_palindrome("python") is False
assert nettoyer(["  Awa ", "KOFFI", "", "  ", "mina"]) == ["awa", "koffi", "mina"]
assert trier_personnes([("Koffi", 25), ("Awa", 20), ("Mina", 25)]) == [("Awa", 20), ("Koffi", 25), ("Mina", 25)]
print("OK")