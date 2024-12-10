import requests
from datetime import datetime

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def is_valid_date(date_text):
    """
    Vérifie si la date est dans le bon format YYYY-MM-DD HH:MM:SS.
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        print("Le format de la date est invalide. Utilisez 'YYYY-MM-DD HH:MM:SS'.")
        return False

def update_subtask(id_subtask,id_affected_task=None, name=None, end_date=None, checked=None):
    """
    Met à jour une sous-tâche en utilisant l'API.

    Paramètres:
    - id_subtask (int) : ID de la sous-tâche.
    - id_affected_task(int) : ID de la tache affecter
    - name (str) : nouveau nom.
    - end_date (str) : nouvelle date de fin au format 'YYYY-MM-DD HH:MM:SS'.
    - checked (int) : état de vérification (1 pour vérifié, 0 pour non vérifié).

    Retourne:
    - Message de succès ou d'erreur.
    """
    if end_date and not is_valid_date(end_date):
        return "La date de fin est invalide. Utilisez le format 'YYYY-MM-DD HH:MM:SS'."

    # Construire les données pour la requête PUT
    post_data = {
        'table': 'Subtask',
        'action': 'update',
        'data': {},
        'column': "id_subtask",
        'value': id_subtask
    }
    if id_subtask:
        post_data['data']['id_subtask'] = id_subtask
    if name:
        post_data['data']['name'] = name
    if end_date:
        post_data['data']['end_date'] = end_date
    if checked is not None:
        post_data['data']['checked'] = checked

    # Vérifier que des champs sont à mettre à jour
    if not post_data['data']:
        return "Aucun champ à mettre à jour."

    # Envoyer la requête PUT à l'API
    try:
        response = requests.put(url, json=post_data)
        if response.status_code == 200:
            return f"Sous-tâche avec ID {id_subtask} mise à jour avec succès."
        else:
            return f"Erreur lors de la mise à jour : {response.status_code} - {response.text}"
    except requests.RequestException as e:
        return f"Erreur de connexion à l'API : {e}"

