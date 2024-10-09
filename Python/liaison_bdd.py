import requests
import json

# URL de l'API PHP
base_url = "http://kicekifeqoa.alwaysdata.net/api.php"


def get_data(table, columns='*'):
    """Récupère les données d'une table spécifique."""
    url = f"{base_url}?table={table}&columns={columns}"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            print(f"Données récupérées depuis la table '{table}':")
            print(json.dumps(data, indent=4))  # Affichage formaté
        else:
            print(f"Erreur lors de la récupération : {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")


def post_data(table, data):
    """Insère des données dans une table spécifique."""
    url = f"{base_url}?table={table}"

    try:
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 201:
            print("Données insérées avec succès :")
            print(response.json())
        else:
            print(f"Erreur lors de l'insertion : {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête : {e}")


if __name__ == "__main__":
    # Exemple de récupération de données
    get_data("Group", "name")  # Remplace "Group" et "name" par la table et les colonnes souhaitées

    # Exemple d'insertion de données
    new_group = {
        'name': 'Nouveau Groupe'  # Remplace par le nom du groupe que tu veux ajouter
    }
    post_data("Group", new_group)  # Remplace "Group" par la table cible
