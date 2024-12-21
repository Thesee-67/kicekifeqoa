import requests
import json
from datetime import datetime

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def update_data(table, data, column, value):
    """ Mise à jour ud'ne entrée dans une table donnée

        Paramètres :
        - table : Nom de la table où mettre à jour les données
        - data : Données à insérer au format dictionnaire
    """
    post_data = {
        'table': table,
        'action': 'update',
        'data': data,
        'column': column,
        'value': value
    }
    response = requests.post(url, json=post_data)
    print(response.json())

def update_group(grp_name, value, column="name"):
    """ Mise à jour d'un  groupe dans la BDD

            Paramètres :
            - grp_name : Nom du groupe à mettre à jour
            - value : Valeur à mettre à jour
            - column : Colonne ou les données doit être mise à jour
    """
    try:
            update_data("Group", {"name":grp_name}, column, value )
            print(f"The value: {value} is update in column: {column} in groupe {grp_name} in table Group")
    except:
        print(f"Error in insertion ")


