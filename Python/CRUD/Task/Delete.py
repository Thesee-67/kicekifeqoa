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
def delete_task(id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Task
        WHERE id_task = %s
    """, (id,))
    conn.commit()

delete_task(1)