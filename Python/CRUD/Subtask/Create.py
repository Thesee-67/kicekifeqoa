import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime

# Configuration de la connexion
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

# Connexion à la base de donnée
conn = connection.MySQLConnection(**config)

def Close_connection_BDD(conn,cursor):
    cursor.close()
    conn.close()

def Insert_sous_task(id_affected_task,name, end_date, checked):
    try:
        # Connexion à la base de données
        cursor = conn.cursor()
        task_exists = check_task_exists(id_affected_task,cursor)
        if task_exists :
            # Requête SQL d'insertion
            sql_insert_query = """
            INSERT INTO Subtask (id_affected_task, name, end_date, checked)
            VALUES (%s, %s, %s, %s)
            """

            # Données à insérer
            data = (id_affected_task,name, end_date, checked)

            # Exécuter la requête et valider les changements
            cursor.execute(sql_insert_query, data)
            conn.commit()

            print(f"Sous-Tâche '{name}' ajoutée avec succès.")
            Close_connection_BDD(cursor, conn)
        else :
            print(f"L'ID {id_affected_task} n'existe pas dans la table Task.")
            Close_connection_BDD(cursor, conn)

    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")

def check_task_exists(id_affected_task,cursor):
    query = "SELECT COUNT(*) FROM Task WHERE id_task = %s"
    cursor.execute(query, (id_affected_task,))
    result = cursor.fetchone()

    # Si le résultat est supérieur à 0, l'ID existe
    if result[0] > 0:
        return True
    else:
        return False

# Exemple d'utilisation
id_affected_task = 1
name = "Appli"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité
tag = "Travail"  # Exemple de tag

Insert_sous_task(id_affected_task,name, end_date, checked)