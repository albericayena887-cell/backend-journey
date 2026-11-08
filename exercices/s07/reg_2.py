import re

mx = re.search(r"ay.*a", "ayena")

if mx:
    print(mx.group())
else:
    print("Correspondance non trouvée")    