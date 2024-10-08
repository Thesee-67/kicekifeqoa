import requests
import json

# URL de ton API PHP (remplace par l'URL réelle de ton API)
url = "https://ton-site.epizy.com/api.php"

try:
    # Envoyer une requête GET à l'API
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Convertir la réponse JSON en objet Python
        data = response.json()

        # Afficher les données récupérées
        print("Données récupérées depuis la base de données :")
        print(json.dumps(data, indent=4))  # Affichage formaté
    else:
        print(f"Erreur : {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête : {e}")
