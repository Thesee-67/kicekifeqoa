import requests
import json

# URL de ton API PHP
url = "http://kicekifeqoa.alwaysdata.net/api.php"


def get_data(table, columns='*', filter_column=None, filter_value=None):
    params = {'table': table, 'columns': columns}

    # Ajouter le filtre s'il est spécifié
    if filter_column and filter_value:
        params['filter_column'] = filter_column
        params['filter_value'] = filter_value

    response = requests.get(url, params=params)
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
# 1. Récupérer toutes les colonnes d'une table
#get_data("Users")

# 2. Récupérer des colonnes spécifiques
#get_data("Users", "email")

# 3. Récupérer des colonnes spécifiques avec un filtre sur une valeur
#get_data("Users", "id_user,email", filter_column="id_user", filter_value="1")

# 4. Récupérer toutes les informations liées à une valeur spécifique (par exemple, nom de personne)
#get_data("Users", "*", filter_column="id_user", filter_value="1")

# Ajouter des données
#add_data("test", {"alpha": "tic","beta": "fax"})

# Mettre à jour des données
#update_data("test", {"beta": "test"}, "beta", "fax")

# Supprimer des données
#delete_data("test", "beta", "fax")
