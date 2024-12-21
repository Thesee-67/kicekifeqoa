import requests
import json
from datetime import datetime

""" URL de base pour l'API """
url = "https://kicekifeqoa.alwaysdata.net/api.php"


def count_data(table, filter_column, filter_value):
    """ Compter les entrées dans une table donnée en fonction d'un filtre

    Paramètres :
    - table : Nom de la table à interroger
    - filter_column : Colonne à utiliser pour filtrer
    - filter_value : Valeur à utiliser pour filtrer la colonne

    Retourne :
    - Résultat en JSON avec le compte, ou False en cas d'erreur
    """

    params = {
        'table': table,
        'filter_column': filter_column,
        'filter_value': filter_value
    }
    response = requests.request("COUNT", url, params=params)
    if response.status_code == 200:
        return json.dumps(response.json(), indent=4)
    else:
        print(f"Erreur : {response.status_code} - {response.text}")
        return False


def verification_doublon_group(name_Group):
    """ Vérifie si un groupe avec le nom donné existe déjà

    Paramètres :
    - name_Group : Nom du groupe à vérifier

    Retourne :
    - True si le groupe n'existe pas, False sinon
    """

    # Vérifier le type et afficher l'argument pour le débogage
    result = count_data('Group', "name", name_Group)
    result = json.loads(result)
    result = result["count"]
    if result is not None:
        # Si le résultat est 0, le name_Group n'existe pas
        if result == 0:
            return True  # Le name_Group n'existe pas, donc il est disponible
        else:
            print("The grp already exists.")
            return False  # Le name_Group existe déjà
    else:
        print("No result found.")
        return True


def add_data(table, data):
    """ Ajoute une nouvelle entrée dans une table donnée

    Paramètres :
    - table : Nom de la table où insérer les données
    - data : Données à insérer au format dictionnaire
    """

    post_data = {
        'table': table,
        'action': 'insert',
        'data': data
    }
    response = requests.post(url, json=post_data)
    print(response.json())


def create_group(grp_name):
    """ Crée un nouveau groupe après avoir vérifié qu'il n'existe pas déjà

    Paramètres :
    - grp_name : Nom du groupe à créer
    """

    try:
        if verification_doublon_group(grp_name):
            add_data("Group", {"name": grp_name})
            print(f"Groupe '{grp_name}' ajoutée avec succès.")
        else:
            print(f"Création du groupe a échoué")

    except:
        print(f"Erreur lors de l'insertion ")


""" Exemple d'utilisation """
name = "ouioui"
end_date = datetime(2024, 10, 15, 18, 0)  # """ Exemple de date et heure de fin """
checked = 0  # """ 0 pour non vérifié, 1 pour vérifié """
priority = 2  # """ Niveau de priorité """
tag = "Travail"  # """ Exemple de tag """

create_group("nonon")
