import requests

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def update_task(id_task, name=None, end_date=None, checked=None, priority=None, tag=None):
    """
    Met à jour une tâche existante en utilisant l'API.
    
    Paramètres:
    - id_task (int) : l'ID de la tâche à mettre à jour.
    - name (str) : nouveau nom de la tâche.
    - end_date (str) : nouvelle date de fin au format 'YYYY-MM-DD HH:MM:SS'.
    - checked (int) : statut vérifié (1) ou non vérifié (0).
    - priority (int) : nouvelle priorité.
    - tag (str) : nouveau tag.
    
    Retourne:
    - Message de succès ou d'erreur.
    """
    data = {
        'table': 'Task',
        'id_task': id_task,
        'update_data': {}
    }

    # Champs à mettre à jour
    if name is not None:
        data['update_data']['name'] = name
    if end_date is not None:
        data['update_data']['end_date'] = end_date
    if checked is not None:
        data['update_data']['checked'] = checked
    if priority is not None:
        data['update_data']['priority'] = priority
    if tag is not None:
        data['update_data']['tag'] = tag

    if not data['update_data']:
        print("Aucun champ à mettre à jour.")
        return

    # Mise à jour avec PUT 
    response = requests.put(url, json=data)

    # Vérifier la réponse de l'API
    if response.status_code == 200:
        return f"Tâche avec ID {id_task} mise à jour avec succès."
    else:
        return f"Erreur lors de la mise à jour : {response.status_code} - {response.text}"

# Test
print(update_task(159, name="Tache2", end_date="2024-10-10 22:02:00", priority=1, tag="Travail"))
