import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl, QObject, Signal, Slot, Property
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


class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine  # Stocker l'instance de l'engine
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.users = []
        self.task_model = TaskModel()  # Associer le modèle de tâches

    # Méthodes pour manipuler les propriétés des tâches depuis QML
    @Slot(str)
    def update_task_name(self, name):
        self.task_name = name

    @Slot(int)
    def update_task_priority(self, priority):
        self.task_priority = priority

    @Slot(str)
    def add_tag(self, tag):
        self.tags.append(tag)
        self.update_tags_in_qml()

    @Slot()
    def remove_last_tag(self):
        if self.tags:
            self.tags.pop()
        self.update_tags_in_qml()

    @Slot(str)
    def add_user(self, email):
        self.users.append(email)
        self.update_users_in_qml()

    @Slot()
    def remove_last_user(self):
        if self.users:
            self.users.pop()
        self.update_users_in_qml()

    def update_tags_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("tagsListModel", self.tags)

    def update_users_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("usersListModel", self.users)

    @Slot()
    def validate_info(self):
        tags_as_string = ", ".join(self.tags)

        # Insertion dans la base de données
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Task (name, end_date, checked, priority, tag) VALUES (%s, %s, %s, %s, %s)",
                (self.task_name, "", 0, self.task_priority, tags_as_string)
            )
            conn.commit()
        except Error as e:
            print(f"Erreur lors de l'insertion de la tâche: {e}")
        finally:
            cursor.close()

        # Afficher les informations dans la console
        print("----- Task Information -----")
        print(f"Task - name: {self.task_name}")
        priority_labels = ["Priorité basse", "Priorité moyenne", "URGENT"]
        print(f"Task - priority: {self.task_priority}")
        print(f"Tags: {tags_as_string}")
        print(f"Users: {self.users}")

        # Recharger les tâches après l'insertion
        self.task_model.load_tasks()


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent

    engine.addImportPath(os.fspath(app_dir))

    # Juste avant de charger l'engine
    task_handler = TaskHandler(engine)  # Passer l'engine ici
    engine.rootContext().setContextProperty("taskHandler", task_handler)
    engine.rootContext().setContextProperty("taskModel", task_handler.task_model)  # Exposer TaskModel

    # Charger le fichier QML
    qml_file = os.fspath(app_dir / 'App.qml')
    engine.load(qml_file)
    if not engine.rootObjects():
        print(f"Erreur lors du chargement de {qml_file}")
        sys.exit(-1)

    # Charger les tâches à l'initialisation
    task_handler.task_model.load_tasks()

    sys.exit(app.exec())
