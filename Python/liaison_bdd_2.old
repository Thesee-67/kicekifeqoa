import pymysql

# Informations de connexion
config = {
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'database': 'kicekifeqoa_todolist'
}


def create_connection():
    """Créer une connexion à la base de données."""
    connection = None
    try:
        connection = pymysql.connect(**config)
        print("Connexion réussie à la base de données")
    except pymysql.MySQLError as e:
        print(f"Erreur lors de la connexion : {e}")
    return connection


def fetch_data(connection):
    """Récupérer des données de la base de données."""
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM `Group`")  # Remplace 'ma_table' par le nom de ta table
        results = cursor.fetchall()

        for row in results:
            print(row)


def main():
    connection = create_connection()

    if connection:
        fetch_data(connection)
        connection.close()
        print("Connexion fermée")


if __name__ == "__main__":
    main()
