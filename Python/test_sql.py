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

# Création d'un curseur
cursor = conn.cursor()

# Exécution d'une requête
query = "SELECT * FROM `Group`"
cursor.execute(query)

# Récupération des résultats
results = cursor.fetchall()

# Affichage des résultats
for row in results:
    print(row)

# Fermeture du curseur et de la connexion
cursor.close()
conn.close()
