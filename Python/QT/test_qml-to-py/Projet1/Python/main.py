import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Signal, Property
import mysql.connector
from mysql.connector import connection, Error

# Configuration pour la connexion MySQL
config = {
    'user': '379269_admin',
    'password': 'Kicekifeqoa123*',
    'host': 'mysql-kicekifeqoa.alwaysdata.net',
    'database': 'kicekifeqoa_todolist',
}

# Connexion à la base de données
try:
    conn = connection.MySQLConnection(**config)
except Error as e:
    print(f"Erreur de connexion à la base de données: {e}")
    sys.exit(1)


class TaskModel(QObject):
    tasksChanged = Signal()

    def __init__(self):
        super(TaskModel, self).__init__()
        self._tasks = []

    @Property(list, notify=tasksChanged)
    def tasks(self):
        return self._tasks

    def load_tasks(self):
        cursor = conn.cursor()
        try:
            # Sélectionner les colonnes nécessaires depuis la table Task
            cursor.execute("SELECT name, end_date, checked, priority, tag FROM Task")

            # Charger les résultats dans une liste de dictionnaires
            self._tasks = [
                {
                    "taskName": row[0],
                    "taskEndDate": str(row[1]),  # Convertir la date en string
                    "taskChecked": bool(row[2]),  # Convertir tinyint en booléen
                    "taskPriority": row[3],
                    "taskTag": row[4]
                }
                for row in cursor.fetchall()
            ]

            # Notifier que les données ont changé
            self.tasksChanged.emit()
        except Error as e:
            print(f"Erreur lors du chargement des tâches: {e}")
        finally:
            cursor.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.task_model = TaskModel()

        # Configurer QML
        self.engine = QQmlApplicationEngine()
        self.engine.rootContext().setContextProperty("taskModel", self.task_model)

        # Charger le fichier QML
        qml_file = 'App.qml'
        self.engine.load(qml_file)

        if not self.engine.rootObjects():
            print(f"Erreur lors du chargement de {qml_file}")
            sys.exit(-1)

        # Charger les tâches
        self.task_model.load_tasks()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec())
