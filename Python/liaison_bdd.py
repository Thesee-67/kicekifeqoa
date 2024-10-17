import requests
import json

# URL de ton API PHP
url = "https://kicekifeqoa.alwaysdata.net/api.php"


def get_data(table, columns='*', filter_column=None, filter_value=None, join_table=None, join_condition=None):
    params = {'table': table, 'columns': columns}

    # Ajouter les filtres s'ils sont spécifiés
    if filter_column and filter_value:
        params['filter_column'] = filter_column
        params['filter_value'] = filter_value

    # Ajouter la jointure si elle est spécifiée
    if join_table and join_condition:
        params['join_table'] = join_table
        params['join_condition'] = join_condition

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
#et_data("Users")

# 2. Récupérer des colonnes spécifiques
#get_data("Users", "email")

# 3. Récupérer des colonnes spécifiques avec un filtre sur une valeur
#get_data("Users", "id_user,email", filter_column="id_user", filter_value="1")

# 4. Récupérer toutes les informations liées à une valeur spécifique (par exemple, nom de personne)
#get_data("Users", "*", filter_column="id_user", filter_value="1")


# 5. Récupérer des données avec une jointure:
#get_data("Task_has_Users", "Task.name,Users.email", join_table="Task,Users", join_condition="Task_has_Users.task_id = Task.id_task,Task_has_Users.user_id = Users.id_user", filter_column="Users.id_user", filter_value="1")

# Ajouter des données
#add_data("test", {"alpha": "tic","beta": "fax"})

# Mettre à jour des données
#update_data("test", {"beta": "test"}, "beta", "fax")

# Supprimer des données
#delete_data("test", "beta", "fax")
