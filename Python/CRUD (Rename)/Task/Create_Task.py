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


def create_task(task_name,end_date,checked,priority,tag):
    try:
        end_date = end_date.strftime('%Y-%m-%d %H:%M:%S')
        add_data("Task", {"name":task_name, "end_date":end_date,"checked":checked, "priority":priority, "tag":tag})
        print(f"Task '{task_name}' ajoutée avec succès.")
    except:
        print(f"Erreur lors de l'insertion ")


# Exemple d'utilisation
name = "ouiouioui"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité
tag = "Travail"  # Exemple de tag

create_task(name,end_date,checked,priority,tag)