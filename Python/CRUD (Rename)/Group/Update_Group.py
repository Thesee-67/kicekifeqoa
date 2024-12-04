import requests
import json
from datetime import datetime

url = "https://kicekifeqoa.alwaysdata.net/api.php"

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

def update_group(grp_name, value, column="name"):
    try:
            update_data("Group", {"name":grp_name}, column, value )
            print(f"The value: {value} is update in column: {column} in groupe {grp_name} in table Group")
    except:
        print(f"Error in insertion ")


# Exemple d'utilisation
name = "ouioui"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité
tag = "Travail"  # Exemple de tag
column2, value2 = "oui" , "oui"
update_group("ouioui", "test")