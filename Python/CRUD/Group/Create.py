import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime

def connection_bdd():
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

def close_connection_bdd(conn,cursor):
    cursor.close()
    conn.close()


def verification_doublon_group(name_Group, cursor):
    # Vérifier le type et afficher l'argument pour le débogage
    # Requête SQL pour vérifier l'existence du groupe
    query = "SELECT COUNT(*) FROM `Group` WHERE name = %s"
    try:
        # Exécution de la requête avec un tuple
        cursor.execute(query, (name_Group,))  # (name_Group,) pour passer en tant que tuple
        # Récupérer le résultat
        result = cursor.fetchone()
        # Vérifier si le résultat est valide
        if result is not None and result[0] is not None:
            # Si le résultat est 0, le name_Group n'existe pas
            if result[0] == 0:
                return True  # Le name_Group n'existe pas, donc il est disponible
            else:
                print("Le groupe existe déjà.")
                return False  # Le name_Group existe déjà
        else:
            print("Aucun résultat trouvé.")
            return True  # Le groupe n'existe pas
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'exécution de la requête : {err}")
        return None  # Indiquer qu'il y a eu une erreur

def create_grp(name):
    try:
        # Connexion à la base de données
        cursor, conn = connection_bdd()
        if verification_doublon_group(name,cursor):
            # Requête SQL d'insertion

            sql_insert_query = """
            INSERT INTO `Group` (name)
            VALUES (%s)
            """
            print(1)
            # Données à insérer
            data = (name,)

            # Exécuter la requête et valider les changements
            cursor.execute(sql_insert_query, data)
            conn.commit()

            print(f"Tâche '{name}' ajoutée avec succès.")
            close_connection_bdd(cursor, conn)

    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")


# Exemple d'utilisation
name = "ouioui"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité
tag = "Travail"  # Exemple de tag

create_grp(name)