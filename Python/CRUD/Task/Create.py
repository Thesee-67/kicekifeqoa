import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime
conn = 0
cursor = 0

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

def insert_task(name, end_date, checked, priority, tag):
    try:
        # Connexion à la base de données
        cursor, conn = Connection_BDD()

        # Requête SQL d'insertion
        sql_insert_query = """
        INSERT INTO Task (name, end_date, checked, priority, tag)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Données à insérer
        data = (name, end_date, checked, priority, tag)

        # Exécuter la requête et valider les changements
        cursor.execute(sql_insert_query, data)
        conn.commit()

        print(f"Tâche '{name}' ajoutée avec succès.")
        Close_connection_BDD(cursor, conn)

    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")


# Exemple d'utilisation
name = "Finir projet"
end_date = datetime(2024, 10, 15, 18, 0)  # Exemple de date et heure de fin
checked = 0  # 0 pour non vérifié, 1 pour vérifié
priority = 2  # Niveau de priorité
tag = "Travail"  # Exemple de tag

insert_task(name, end_date, checked, priority, tag)