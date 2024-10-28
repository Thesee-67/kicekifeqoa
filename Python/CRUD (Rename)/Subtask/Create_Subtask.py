import requests
import json
from datetime import datetime
url = "https://kicekifeqoa.alwaysdata.net/api.php"

def add_data(table, data):
    post_data = {
        'table': table,
        'action': 'insert',
        'data': data
    }
    response = requests.post(url, json=post_data)
    print(response.json())
def count_data(table, filter_column, filter_value):

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

def verification_id_sub_task(id_affected_task):
    # Vérifier le type et afficher l'argument pour le débogage
    result = count_data ('Task',"id_task", id_affected_task)
    result = json.loads(result)
    result = result["count"]
    if result is not None:
        # Si le résultat est 0, le id_sub_task n'existe pas
        if result != 0:
            return True  # Le id_sub_task existe, donc il est disponible
        else:
            print("The id_sub_task No already exists.")
            return False  # Le id_sub_task n'existe pas
    else:
        print("No result found.")
        return False


def create_subtask(subtask_name,id_affected_task,end_date,checked,priority):
    try:
        if verification_id_sub_task(id_affected_task):
            end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
            add_data("Subtask", {"id_affected_task":id_affected_task,"name":subtask_name, "end_date":end_date,"checked":checked})
            print(f"Task '{subtask_name}' ajoutée avec succès.")
        else:
            print("No task fund")
    except:
        print(f"Erreur lors de l'insertion ")


# Exemple d'utilisation
id_affected_task = 1
name = "ouiouioui"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité


create_subtask(name,id_affected_task,end_date,checked,priority)