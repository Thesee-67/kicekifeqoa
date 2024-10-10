import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime
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

def Close_connection_BDD(conn,cursor):
    cursor.close()
    conn.close()

def insert_task(table, data):
    try:
        post_data = {
            'table': table,
            'action': 'insert',
            'data': data
        }
        response = requests.post(url, json=post_data)
        print(response.json())

    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")

# Ajouter des données
#add_data("Task", {"name": "tache","end_date": "","checked": "0","priority": "0","tag": "Travail"})
insert_task("Task", {"name": "Tache1","end_date": "2024-10-10 22:02:00","checked": "0","priority": "0","tag": "Travail"})