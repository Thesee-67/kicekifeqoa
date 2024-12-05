import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime
import requests
import json

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
    print("La connexion à la base de données a été fermée.")

def create_task(table, data):
    try:
        post_data = {
            'table': table,
            'action': 'insert',
            'data': data
        }
        response = requests.post(url, json=post_data)
        # Vérifier le code de statut pour voir si la requête a réussi
        if response.status_code == 200:
            result = response.json()

            # Vérifier si l'ID de la tâche est retourné dans la réponse
            if 'id_task' in result:
                task_id = result['id_task']
                print(f"Tâche créée avec succès. ID de la tâche : {task_id}")
                return task_id
            else:
                raise ValueError("L'ID de la tâche n'a pas été retourné dans la réponse.")
        else:
            raise ValueError(f"Erreur lors de la création de la tâche : {response.status_code}")
    except Exception as e:
        print(f"Erreur : {e}")
        return None

create_task("Task", {
    "name": 'Test',
    "end_date": '2024-12-22',
})