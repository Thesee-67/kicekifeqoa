from mysql.connector import (connection)
from mysql.connector import Error

# URL de ton API PHP
url = "https://kicekifeqoa.alwaysdata.net/api.php"

# Configuration de la connexion
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

def get_tasks():
    # Connexion à la base de données
    conn = connection.MySQLConnection(**config)
    cursor = conn.cursor()

    # Requête pour récupérer les données
    cursor.execute('SELECT id_task, name, end_date, checked, priority, tag FROM Task')
    tasks = cursor.fetchall()

    # Renvoie les tâches sous forme de liste de dictionnaires
    return [{"id_task": task[0], "name": task[1], "end_date": task[2], "checked": task[3], "priority": task[4], "tag": task[5]} for task in tasks]
