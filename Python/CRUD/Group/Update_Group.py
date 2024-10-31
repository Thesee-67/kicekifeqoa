import requests

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def update_group(id_group, name=None, description=None):
    """
    Met à jour un groupe en utilisant l'API.

    Paramètres:
    - id_group (int) : ID du groupe.
    - name (str) : nouveau nom du groupe.
    - description (str) : nouvelle description du groupe.

    Retourne:
    - Message de succès ou d'erreur.
    """

    data = {
        'table': 'Group',
        'id_group': id_group,
        'update_data': {}
    }

    # Ajouter les champs à mettre à jour
    if name:
        data['update_data']['name'] = name
    if description:
        data['update_data']['description'] = description

    # Vérifier que des champs sont à mettre à jour
    if not data['update_data']:
        return "Aucun champ à mettre à jour."

    # Envoyer la requête PUT à l'API
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return f"Groupe avec ID {id_group} mis à jour avec succès."
        else:
            return f"Erreur lors de la mise à jour : {response.status_code} - {response.text}"
    except requests.RequestException as e:
        return f"Erreur de connexion à l'API : {e}"

# Test
print(update_group(3, name="Nouveau Groupe", description="Description mise à jour"))
