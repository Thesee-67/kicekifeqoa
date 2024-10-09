import requests
import json

# URL de ton API PHP
base_url = "http://kicekifeqoa.alwaysdata.net/api.php"

def fetch_data(table_name, columns):
    try:
        # Construire l'URL avec les paramètres de table et colonnes
        url = f"{base_url}?table={table_name}&columns={columns}"

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
            print(f"Données récupérées depuis la table {table_name} :")
            print(json.dumps(data, indent=4))  # Affichage formaté
        else:
            print(f"Erreur : {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

# Appel de la fonction pour récupérer uniquement le champ 'name'
fetch_data('Group', 'name')
