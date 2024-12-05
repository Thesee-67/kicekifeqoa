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

def get_task(id_task=None, name=None, end_date=None, checked=None, priority=None, tag=None):
    """
    Permet de récupérer les information d'une ou plusieurs taches en fonction des paramètres entrer
    Si aucun paramètres n'est entrer retourne TOUTES les tache (Peu recommander)
    Si une id est entrer retourne une seul tache
    Si plusieur taches coresspondes au paramètres retourne plusieurs taches
    (ex name="toto",tag="titi")

    paramètres:
    id_task: int
    name : str
    end_date : str format YYYY-MM-JJ HH:mm:SS
    checked : int (1 ou 0)
    priority : int
    tag :str

    retourne une liste de dictionaire (key = nom colone, value = valeur)
    ex {'id_task':135}
    Si aucune correspondance trouver avec tout les pramètres entrer retourne 'no existing links'
    """
    if id_task != None:
        return get_data("Task",filter_column="id_task",filter_value=id_task)
    else:
        columns = {
            "id_task": id_task,
            "name": name,
            "end_date": end_date,
            "checked": checked,
            "priority": priority,
            "tag": tag
        }
        filters = {col: value for col, value in columns.items() if value is not None}
        if len(filters) == 1:
            col, val = next(iter(filters.items()))
            data = get_data("Task", filter_column=col, filter_value=val)
            if data != []:
                return data
            else:
                return 'no existing links'
        elif len(filters) == 2:
            list =[]
            filter_col, filter_val = zip(*filters.items())
            data = get_data("Task",filter_column=filter_col[0],filter_value=filter_val[0])
            for task in data:
                if (task[filter_col[1]] == filter_val[1]):
                    list.append(task)
            if list != []:
                return list
            else:
                return "no existing links"
        elif len(filters) == 3:
            list =[]
            filter_col, filter_val = zip(*filters.items())
            data = get_data("Task", filter_column=filter_col[0], filter_value=filter_val[0])
            for task in data:
                if (task[filter_col[1]] == filter_val[1]) and (task[filter_col[2]] == filter_val[2]):
                    list.append(task)
            if list != []:
                return list
            else:
                return "no existing links"
        elif len(filters) == 4:
            list =[]
            filter_col, filter_val = zip(*filters.items())
            data = get_data("Task", filter_column=filter_col[0], filter_value=filter_val[0])
            for task in data:
                if (task[filter_col[1]] == filter_val[1]) and (task[filter_col[2]] == filter_val[2]) and (task[filter_col[3]] == filter_val[3]):
                    list.append(task)
            if list != []:
                return list
            else:
                return "no existing links"
        elif len(filters) == 5:
            list =[]
            filter_col, filter_val = zip(*filters.items())
            data = get_data("Task", filter_column=filter_col[0], filter_value=filter_val[0])
            for task in data:
                if (task[filter_col[1]] == filter_val[1]) and (task[filter_col[2]] == filter_val[2]) and (task[filter_col[3]] == filter_val[3]) and (task[filter_col[4]] == filter_val[4]):
                    list.append(task)
            if list != []:
                return list
            else:
                return "no existing links"
        else:
            return get_data("Task")


def get_taskid(name=None, end_date=None):
    """
    Permet de récupérer l'ID d'une tâche en fonction du nom et de la date de fin spécifiés.
    Si plusieurs tâches correspondent à ces critères, retourne les ID des tâches correspondantes.
    """
    if name is not None and end_date is not None:
        # Créer un dictionnaire de filtres
        filters = [
            ("name", name),
            ("end_date", end_date)
        ]

        # Appel à get_data avec les filtres passés comme paramètres
        data = get_data("Task", columns="id_task", filters=filters)

        if data and isinstance(data, list):  # Si des tâches sont trouvées
            return [task['id_task'] for task in data]  # Retourne les ID des tâches
        else:
            return 'no existing links'
    else:
        return 'Nom ou date de fin manquants.'







