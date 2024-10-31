import requests
import re

url = "https://kicekifeqoa.alwaysdata.net/api.php"

def is_valid_email(email):
    """
    Vérifie si l'email est dans un format valide.
    """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    else:
        print("Format d'email invalide.")
        return False

def Compliance_password(password):
    """
    Vérifie la conformité et la sécurité du mot de passe.
    """
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule.")
        return False
    if not re.search(r"[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule.")
        return False
    if not re.search(r"[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
        return False
    return True

def update_user(id_user, email=None, password=None, name=None):
    """
    Met à jour un utilisateur en utilisant l'API.

    Paramètres:
    - id_user (int) : ID de l'utilisateur.
    - email (str) : nouvel email.
    - password (str) : nouveau mot de passe.
    - name (str) : nouveau nom.

    Retourne:
    - Message de succès ou d'erreur.
    """
    # Validation des champs
    if email and not is_valid_email(email):
        return "L'email fourni est invalide."
    if password and not Compliance_password(password):
        return "Le mot de passe fourni est trop faible."

    # Construire les données pour la requête PUT
    data = {
        'table': 'Users',
        'id_user': id_user,
        'update_data': {}
    }
    if email:
        data['update_data']['email'] = email
    if password:
        data['update_data']['password'] = password
    if name:
        data['update_data']['name'] = name

    # Vérifier que des champs sont à mettre à jour
    if not data['update_data']:
        return "Aucun champ à mettre à jour."

    # Envoyer la requête PUT à l'API
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return f"Utilisateur avec ID {id_user} mis à jour avec succès."
        else:
            return f"Erreur lors de la mise à jour : {response.status_code} - {response.text}"
    except requests.RequestException as e:
        return f"Erreur de connexion à l'API : {e}"

# Test
print(update_user(159, email="nouveau.email@example.com", password="NouveauMDP!123", name="Nouveau Nom"))
