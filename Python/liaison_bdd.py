import requests
import json

# URL de ton API PHP
url = "http://kicekifeqoa.alwaysdata.net/api.php"

try:
    # Envoyer une requête GET
    response = requests.get(url, timeout=10)

    # Afficher le contenu brut de la réponse
    print("Contenu brut de la réponse :")
    print(response.text)

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
