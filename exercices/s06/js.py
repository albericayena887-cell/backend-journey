import json
import requests

# URL officielle et ultra-fiable pour tester le code
url = "https://jsonplaceholder.typicode.com"
response = requests.get(url)

data = response.json()

# Affichage propre dans la console
print(json.dumps(data, indent=2))
