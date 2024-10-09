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
def delete_group(id):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM Group
        WHERE id_group = %s
    """, (id,))
    conn.commit()