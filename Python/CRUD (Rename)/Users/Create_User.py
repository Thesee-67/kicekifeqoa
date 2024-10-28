import re
import dns.resolver
import requests
import json
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

def verification_email(email):
    # Vérifier le type et afficher l'argument pour le débogage
    result = count_data ('Users',"email", email)
    result = json.loads(result)
    result = result["count"]
    # Si le résultat est 0, le email n'existe pas
    if result == 0:
        return True  # Le email n'existe pas, donc il est disponible
    else:
        print("The grp already exists.")
        return False  # Le email existe déjà

def compliance_password(Password) :
    if len(Password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
        return False
    #Il faut enlevé les , des false et mettre des print pour les erreurs
    """if not re.search(r"[A-Z]", Password):
        return False, "Le mot de passe doit contenir au moins une lettre majuscule."
    if not re.search(r"[a-z]", Password):
        return False, "Le mot de passe doit contenir au moins une lettre minuscule."
    if not re.search(r"[0-9]", Password):
        return False, "Le mot de passe doit contenir au moins un chiffre."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", Password):
        return False, "Le mot de passe doit contenir au moins un caractère spécial."""""

    return True


def is_valid_email(email):
    # Vérification du format de l'email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(regex, email):
        print("Format d'email invalide.")
        return False

    # Vérification de l'existence du domaine
    domain = email.split('@')[-1]
    try:
        # Vérifier les enregistrements MX du domaine
        dns.resolver.resolve(domain, 'MX')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print("Le domaine de l'email n'existe pas.")
        return False
    return True

def create_user (E_mail,Password):
    try:

        if (verification_email (E_mail)
                and compliance_password(Password) and is_valid_email(E_mail)):
            add_data("Users",
                     {"email": E_mail, "password": Password})
            print(f"Creation user : {E_mail} succes.")

    except:
        print(f"Erreur lors de l'insertion ")


# Exemple d'utilisation
E_mail = "jorikbaumert86@gmail.com"
Password = "12345678"
create_user(E_mail,Password)
