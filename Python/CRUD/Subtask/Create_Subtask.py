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

def create_subtask(table, data):
    try:
        post_data = {
            'table': table,
            'action': 'insert',
            'data': data
        }
        response = requests.post(url, json=post_data)
        print(response.json())
        close_connection_BDD(conn, cursor)
    except Error as e:
        print(f"Erreur lors de l'insertion : {e}")
