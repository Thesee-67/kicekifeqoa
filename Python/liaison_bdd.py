import requests
import json

# URL de ton API PHP
url = "http://kicekifeqoa.alwaysdata.net/api.php"

def get_data(table, columns='*'):
    response = requests.get(url, params={'table': table, 'columns': columns})
    if response.status_code == 200:
        print("Données récupérées :")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")

def add_data(table, data):
    post_data = {
        'table': table,
        'action': 'insert',
        'data': data
    }
    response = requests.post(url, json=post_data)
    print(response.json())

def update_data(table, data, column, value):
    post_data = {
        'table': table,
        'action': 'update',
        'data': data,
        'column': column,
        'value': value
    }
    response = requests.post(url, json=post_data)
    print(response.json())

def delete_data(table, column, value):
    post_data = {
        'table': table,
        'column': column,
        'value': value
    }
    response = requests.delete(url, json=post_data)
    print(response.json())

# Exemples d'utilisation
# Récupérer des données avec des colonnes spécifiques
get_data("test", "alpha,beta")

# Ajouter des données
#add_data("test", {"alpha": "tic","beta": "fax"})

# Mettre à jour des données
#update_data("test", {"beta": "test"}, "beta", "fax")

# Supprimer des données
#delete_data("test", "beta", "fax")
