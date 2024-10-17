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

def get_users(id_user=None,email=None,password=None):
    """
    Permet de récupérer les information d'un ou plusieurs utilisateur
    Si aucun paramètre n'est entrée retourne TOUT les utilisateur (peu recoomander)
    Si id_user est entrer retourne un seul utilisateur
    Si plusieur utilisateurs coresspondes au paramètres retourne plusieurs utilisateurs

    paramètres:
    id_user: int
    email: str
    password: str

    Retourne une liste de dictionaire
    Si aucune correspondance trouver avec tout les pramètres entrer retourne 'no existing links'
    """
    if id_user != None:
        data = get_data("Users", filter_column="id_user", filter_value=id_user)
        if data != []:
            return data
        else:
            return 'no existing links'
    elif email != None and password != None:
        list =[]
        data = get_data("Users", filter_column="email", filter_value=email)
        for task in data:
            if (task["password"] == password):
                list.append(task)
        if list != []:
            return list
        else:
            return "no existing links"
    elif email != None:
        data = get_data("Users", filter_column="email", filter_value=email)
        if data != []:
            return data
        else:
            return 'no existing links'
    elif password != None:
        data = get_data("Users", filter_column="password", filter_value=password)
        if data != []:
            return data
        else:
            return 'no existing links'
    else:
        return get_data("Users")