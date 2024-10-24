import mysql.connector
from mysql.connector import (connection)
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
    print("La connexion à la base de données a été fermée.")

def update_subtask(table, id_column, id_value, update_data):
    """
    Met à jour une sous-tâche dans la base de données.

    table : str
        Le nom de la table à mettre à jour (ici "Subtask").
    id_column : str
        Le nom de la colonne qui identifie la sous-tâche à mettre à jour (ex. "id_subtask").
    id_value : str/int
        La valeur de cette colonne pour la sous-tâche à mettre à jour.
    update_data : dict
        Un dictionnaire contenant les colonnes à mettre à jour et leurs nouvelles valeurs.
    """
    try:
        post_data = {
            'table': table,
            'action': 'update',
            'id_column': id_column,
            'id_value': id_value,
            'data': update_data
        }
        # Envoie de la requête PUT à l'API pour la mise à jour
        response = requests.put(url, json=post_data)
        print(response.json())
        Close_connection_BDD(conn, cursor)
    except mysql.connector.Error as e:
        print(f"Erreur lors de la mise à jour : {e}")