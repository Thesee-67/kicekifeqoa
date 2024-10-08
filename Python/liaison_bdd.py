import requests
import json

# URL de ton API PHP
url = "http://kicekifeqoa.infinityfreeapp.com/api.php"

# Ajouter un en-tête User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Envoyer une requête GET avec un User-Agent
    response = requests.get(url, headers=headers, timeout=10)

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
