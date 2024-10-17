import mysql.connector
from mysql.connector import (connection)
from mysql.connector import Error
from datetime import datetime
conn = 0
cursor = 0

def Connection_BDD():
    config = {
        'user': '379269_admin',
        'password': 'Kicekifeqoa123*',
        'host': 'mysql-kicekifeqoa.alwaysdata.net',
        'database': 'kicekifeqoa_todolist',
    }
    conn = connection.MySQLConnection(user='379269_admin', password='Kicekifeqoa123*',
                                      host='mysql-kicekifeqoa.alwaysdata.net',
                                      database='kicekifeqoa_todolist')
    cursor = conn.cursor()
    return cursor, conn

def Close_connection_BDD(conn,cursor):
    cursor.close()
    conn.close()


def update_task(task_id, name=None, end_date=None, checked=None, priority=None, tag=None):
    try:
        cursor, conn = Connection_BDD()

        update_fields = []
        values = []

        if name is not None:
            update_fields.append("name = %s")
            values.append(name)

        if end_date is not None:
            update_fields.append("end_date = %s")
            values.append(end_date)

        if checked is not None:
            update_fields.append("checked = %s")
            values.append(checked)

        if priority is not None:
            update_fields.append("priority = %s")
            values.append(priority)

        if tag is not None:
            update_fields.append("tag = %s")
            values.append(tag)

        if not update_fields:
            print("Aucune mise à jour n'a été spécifiée.")
            return

        sql_update_query = f"""
        UPDATE Task
        SET {', '.join(update_fields)}
        WHERE id = %s
        """
        values.append(task_id)

        cursor.execute(sql_update_query, tuple(values))
        conn.commit()

        print(f"Tâche avec ID {task_id} mise à jour avec succès.")
        Close_connection_BDD(conn, cursor)

    except Error as e:
        print(f"Erreur lors de la mise à jour : {e}")
