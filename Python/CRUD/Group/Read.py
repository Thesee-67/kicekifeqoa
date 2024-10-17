import requests

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
        return response.json()
    else:
        return(f"Erreur : {response.status_code} - {response.text}")


def get_group(id_group=None,name=None):
    """
    Permet de récupérer les information d'un ou plisueur groupe
    Si aucun paramètre n'est entrée retourne TOUT les groupes (peu recoomander)

    paramètres:
    id_group: int
    name: str

    Retourne une liste de dictionaire
    Si aucune correspondance trouver avec tout les pramètres entrer retourne 'no existing links'
    """
    if id_group != None:
        data = get_data("Group", filter_column="id_group", filter_value=id_group)
        if data != []:
            return data
        else:
            return 'no existing links'
    elif name != None:
        data = get_data("Group", filter_column="name", filter_value=name)
        if data != []:
            return data
        else:
            return 'no existing links'
    else:
        return get_data("Group")
