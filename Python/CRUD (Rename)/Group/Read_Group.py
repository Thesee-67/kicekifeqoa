import requests
import json
def get_data(table, columns='*', filter_column=None, filter_value=None, join_table=None, join_condition=None):
    params = {'table': table, 'columns': columns}
    url = "http://kicekifeqoa.alwaysdata.net/api.php"
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

def count_data(table, filter_column, filter_value):
    url = "https://kicekifeqoa.alwaysdata.net/api.php"
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

def get_group (id_group=None, name_group=None):
    if id_group is not None:
        return get_data("Group",filter_column="id_group",filter_value=id_group)
    elif name_group is not None:
        result = count_data("Group","name",name_group)
        result = json.loads(result)
        result = result["count"]
        if result >= 1:
            if result == 1:
                return get_data("Group",filter_column="name",filter_value=name_group)
            elif result >=2:
                list=[]
                for task in result:
                    list.append(task)
                if list != []:
                    return  list
        else:
            print("name Group invalid")
    else:
        print("ID Group invalid")