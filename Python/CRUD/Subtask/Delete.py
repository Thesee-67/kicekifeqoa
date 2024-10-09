import mysql.connector
from mysql.connector import (connection)

# Configuration de la connexion
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

# Connexion à la base de donnée
conn = connection.MySQLConnection(**config)
def delete_subtask(id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Subtask
        WHERE id_subtask = %s
    """, (id,))
    conn.commit()