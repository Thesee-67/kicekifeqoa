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

def insert_task_user_association(task_id, user_id):
    # Connexion à la base de données
    conn = sqlite3.connect("your_database.db")  # Remplace par le chemin correct vers ta base de données
    cursor = conn.cursor()

    # Insertion dans la table Task_has_Users
    try:
        cursor.execute("""
            INSERT INTO Task_has_Users (task_id, user_id)
            VALUES (?, ?)
        """, (task_id, user_id))

        # Commit pour appliquer les changements
        conn.commit()
        print(f"Tâche {task_id} associée à l'utilisateur {user_id}")

    except sqlite3.IntegrityError as e:
        print(f"Erreur d'intégrité : {e}")  # Gestion des erreurs si les clés sont en conflit

    finally:
        conn.close()