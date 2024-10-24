import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime
import json
import requests

# URL de ton API PHP
url = "https://kicekifeqoa.alwaysdata.net/api.php"

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

def close_connection_BDD(conn,cursor):
    cursor.close()
    conn.close()

def create_subtask(id_affected_task,name, end_date, checked):
    try:
        # Connexion à la base de données
        task_exists = check_task_exists(id_affected_task,cursor)
        if task_exists :
            post_data = {
                'table': table,
                'action': 'insert',
                'data': data
            }
            response = requests.post(url, json=post_data)
            close_connection_BDD(cursor, conn)
        else :
            print(f"L'ID {id_affected_task} n'existe pas dans la table Task.")
            close_connection_BDD(cursor, conn)

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
