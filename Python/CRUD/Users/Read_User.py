import requests
import json

# URL de ton API PHP
url = "https://kicekifeqoa.alwaysdata.net/api.php"


def get_data(table, columns='*', filter_column=None, filter_value=None, filter_column2=None, filter_value2=None, join_table=None, join_condition=None):
    params = {'table': table, 'columns': columns}

    # Ajouter le premier filtre s'il est spécifié (ex: email)
    if filter_column and filter_value:
        params['filter_column'] = filter_column
        params['filter_value'] = filter_value

    # Ajouter le deuxième filtre s'il est spécifié (ex: password)
    if filter_column2 and filter_value2:
        params['filter_column2'] = filter_column2
        params['filter_value2'] = filter_value2

    # Ajouter la jointure si elle est spécifiée
    if join_table and join_condition:
        params['join_table'] = join_table
        params['join_condition'] = join_condition

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Retourner les données pour les utiliser dans checkCredentials
    else:
        print(f"Erreur : {response.status_code} - {response.text}")
        return None  # Retourner None en cas d'erreur
