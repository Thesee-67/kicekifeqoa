import requests
import json
from datetime import datetime

from shiboken6.Shiboken import delete

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def delete_data(table, column, value):
    """ Supprime un groupe  dans une table donnée

        Paramètres :
        - table : Nom de la table où supprimer les données
        - data : Données à supprimer au format dictionnaire
    """
    post_data = {
        'table': table,
        'column': column,
        'value': value
    }
    response = requests.delete(url, json=post_data)
    print(response.json())

def delete_group( value, column = "name"):
    """ Supprimer un  groupe dans la BDD

        Paramètres :
        - grp_name : Nom du groupe à Supprimer
        """
    try :
        delete_data("Group", column, value)
    except :
        print("Impossible to delete check if the Group exist")

delete_group("nonon")