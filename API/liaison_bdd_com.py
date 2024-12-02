import requests
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# URL de votre API PHP
url = "https://kicekifeqoa.alwaysdata.net/api_2.php"

# Clé de chiffrement (doit être de 32 octets pour AES-256)
KEY = bytes.fromhex("ad7f252117bc9633183efaae5e33aaf08530610f7bc8bc7e19f1a3ca96f64e00")  # Vérifiez si elle fait 32 octets
IV = b'0123456789abcdef'  # IV fixe (doit être identique entre le client et le serveur)


# Fonction pour chiffrer les données
def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    return base64.b64encode(ciphertext).decode()


# Fonction pour déchiffrer les données
def decrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted_data = unpad(cipher.decrypt(base64.b64decode(data)), AES.block_size)
    return decrypted_data.decode()


# Exemple de fonction de requête GET avec chiffrement
def get_data(table, columns='*', filter_column=None, filter_value=None, join_table=None, join_condition=None):
    params = {'table': table, 'columns': columns}

    if filter_column and filter_value:
        params['filter_column'] = filter_column
        params['filter_value'] = filter_value

    if join_table and join_condition:
        params['join_table'] = join_table
        params['join_condition'] = join_condition

    encrypted_params = encrypt_data(json.dumps(params))
    response = requests.get(url, data={'data': encrypted_params})

    print("Paramètres chiffrés :", encrypted_params)

    if response.status_code == 200:
        decrypted_response = decrypt_data(response.text)
        print("Données récupérées :", json.loads(decrypted_response))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")


def add_data(table, data):
    post_data = {
        'table': table,
        'action': 'insert',
        'data': data
    }
    encrypted_post_data = encrypt_data(json.dumps(post_data))
    response = requests.post(url, data={'data': encrypted_post_data})

    if response.status_code == 200:
        decrypted_response = decrypt_data(response.text)
        print(json.loads(decrypted_response))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")


def update_data(table, data, column, value):
    post_data = {
        'table': table,
        'action': 'update',
        'data': data,
        'column': column,
        'value': value
    }
    encrypted_post_data = encrypt_data(json.dumps(post_data))
    response = requests.post(url, data={'data': encrypted_post_data})

    if response.status_code == 200:
        decrypted_response = decrypt_data(response.text)
        print(json.loads(decrypted_response))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")


def delete_data(table, column, value):
    post_data = {
        'table': table,
        'column': column,
        'value': value
    }
    encrypted_post_data = encrypt_data(json.dumps(post_data))
    response = requests.delete(url, data={'data': encrypted_post_data})

    if response.status_code == 200:
        decrypted_response = decrypt_data(response.text)
        print(json.loads(decrypted_response))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")


def count_data(table, filter_column, filter_value):
    params = {
        'table': table,
        'filter_column': filter_column,
        'filter_value': filter_value
    }
    encrypted_params = encrypt_data(json.dumps(params))
    response = requests.request("GET", url, data={'data': encrypted_params})  # Use GET for counting

    if response.status_code == 200:
        decrypted_response = decrypt_data(response.text)
        print("Nombre d'occurrences :", json.loads(decrypted_response))
    else:
        print(f"Erreur : {response.status_code} - {response.text}")

# Exemples d'utilisation
# 1. Récupérer toutes les colonnes d'une table
get_data("Group")

# 2. Récupérer des colonnes spécifiques
#get_data("Users", "email")

# 3. Récupérer des colonnes spécifiques avec un filtre sur une valeur
#get_data("Task", filter_column="checked", filter_value="1")

# 4. Récupérer toutes les informations liées à une valeur spécifique (par exemple, nom de personne)
#get_data("Users", "*", filter_column="id_user", filter_value="1")

# 5. Récupérer des données avec une jointure:
#get_data("Task_has_Users", "Task.name,Users.email", join_table="Task,Users", join_condition="Task_has_Users.task_id = Task.id_task,Task_has_Users.user_id = Users.id_user", filter_column="Users.id_user", filter_value="1")

# Ajouter des données
#add_data("test", {"alpha": "tic","beta": "fax"})

# Mettre à jour des données
#update_data("test", {"beta": "test"}, "beta", "fax")

# Supprimer des données
#delete_data("test", "beta", "fax")

#Compter les Occurences
#count_data("Group", "name", "ouioui")