import re
import dns.resolver
from mysql.connector import (connection)
from mysql.connector import Error


def Connection_BDD():
    config = {
        'user': '379269_admin',
        'password': 'Kicekifeqoa123*',
        'host': 'mysql-kicekifeqoa.alwaysdata.net',
        'database': 'kicekifeqoa_todolist',
    }
    conn = connection.MySQLConnection(user='379269_admin', password='Kicekifeqoa123*',
                                      host='mysql-kicekifeqoa.alwaysdata.net',
                                      database='kicekifeqoa_todolist')
    cursor = conn.cursor()
    return cursor, conn

def Close_connection_BDD(conn,cursor):
    cursor.close()
    conn.close()

def Verfication_doublon_email (E_mail, cursor):
    # Requête SQL pour vérifier l'existence de l'email
    query = "SELECT COUNT(*) FROM Users WHERE email = %s"
    cursor.execute(query, (E_mail,))
    result = cursor.fetchone()

    # Si le résultat est 0, l'email n'existe pas
    if result[0] == 0:
        return True  # L'email n'existe pas, donc il est disponible
    else:
        print("The email already exists")
        return False  # L'email existe déjà

def Compliance_password(Password) :
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

def Creation_user (E_mail,Password):
    try:
        # Connexion à la base de données
        cursor, conn = Connection_BDD()
        if (Verfication_doublon_email (E_mail,cursor)
                and Compliance_password(Password) and is_valid_email(E_mail)):

            # Requête SQL d'insertion
            sql_insert_query = """
            INSERT INTO Users (email, password)
            VALUES (%s, %s)
            """
            # Données à insérer
            data = (E_mail,Password)

            # Exécuter la requête et valider les changements
            cursor.execute(sql_insert_query, data)
            conn.commit()

            print(f"Creation user : {E_mail} succes.")
            Close_connection_BDD(cursor, conn)

    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")


# Exemple d'utilisation
E_mail = "jorikbaumert86@gmail.com"
Password = "12345678"
Creation_user(E_mail,Password)
