import re
import dns.resolver
from mysql.connector import (connection)
from mysql.connector import Error
import requests
import json

# URL de ton API PHP
url = "http://kicekifeqoa.alwaysdata.net/api.php"

# Configuration de la connexion
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

# Connexion à la base de donnée
conn = connection.MySQLConnection(**config)
cursor = conn.cursor()

def Close_connection_BDD(conn, cursor):
    cursor.close()
    conn.close()

def Duplicate_email_check(email, cursor, user_id=None):
    """
    Vérifie si un email existe déjà dans la base de données.
    Si user_id est fourni, exclut l'utilisateur actuel de la vérification.
    """
    if user_id:
        query = "SELECT COUNT(*) FROM Users WHERE email = %s AND id_user != %s"
        cursor.execute(query, (email, user_id))
    else:
        query = "SELECT COUNT(*) FROM Users WHERE email = %s"
        cursor.execute(query, (email,))
    result = cursor.fetchone()
    return result[0] == 0

def Compliance_password(password):

    if len(password) < 8:
        print("Le mot de passse doit contenir au moins 8 caractères.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Le mot de passe doit contenir au moins une lettre majuscule. ")
        return False
    if not re.search(r"[a-z]", password):
        print("Le mot de passe doit contenir au moins une lettre minuscule. ")
        return False
    if not re.search(r"[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre. ")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial. ")
        return False
    return True

def is_valid_email(email):
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

def Update_user(user_id, update_data):
    try:
        cursor = conn.cursor()

        if 'email' in update_data:
            new_email = update_data['email']
            if not is_valid_email(new_email) or not Duplicate_email_check(new_email, cursor, user_id):
                print(f"Impossible de mettre à jour l'email, veuillez entrer un ID Utilisateur ou une adresse email valide. ")
                return

        if 'password' in update_data:
            new_password = update_data['password']
            if not Compliance_password(new_password):
                print(f"Impossible de mettre le mot de passe à jour. ")
                return
        set_clause = ', '.join([f"{key} = %s" for key in update_data.keys()])
        sql_update_query = f"UPDATE Users SET {set_clause} WHERE id_user = %s"

        data = tuple(update_data.values()) + (user_id,)

        cursor.execute(sql_update_query, data)
        conn.commit()

        print(f"Utilisateur {user_id} mis à jour !")
        Close_connection_BDD(conn, cursor)

    except Error as e:
        print(f"Erreur lors de la mise à jour : {e}")
    finally:
        Close_connection_BDD(conn, cursor)

# Test
Update_user(5, {"email": "kiki@jonj.jaj", "password": "NouveauMotDePasse123!"})





