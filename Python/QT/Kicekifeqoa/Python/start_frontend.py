import os
import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl, QObject, Signal, Slot

from Python.CRUD.Subtask.Create import end_date  # Assurez-vous que cette importation est nécessaire
from autogen.settings import url, import_paths
from Python.CRUD.Task.Create import insert_task


class TaskHandler(QObject):
    """
    Classe qui gère la création et la manipulation des tâches.
    Elle communique avec l'interface QML via des Slots.
    """

    def __init__(self, engine):
        """ Initialise les attributs et l'intégration avec le moteur QML. """
        super().__init__()
        self.engine = engine
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.users = []
        self.start_date = None
        self.end_date = None

    @Slot(str)
    def add_task_name(self, taskname):
        """ Définit le nom de la tâche. """
        if taskname.strip():
            self.task_name = taskname
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

    @Slot(int)
    def add_task_priority(self, priority):
        """ Définit la priorité de la tâche. """
        if priority in [0, 1, 2]:  # 0: Basse, 1: Moyenne, 2: Urgente
            self.task_priority = priority
        else:
            print("Erreur : Priorité invalide.")

    @Slot(str)
    def add_tag(self, tag):
        """ Ajoute un tag à la liste des tags. """
        if tag.strip():
            self.tags.append(tag)
            self._update_tags_in_qml()
        else:
            print("Erreur : Tag invalide.")

    @Slot()
    def remove_last_tag(self):
        """ Retire le dernier tag ajouté. """
        if self.tags:
            self.tags.pop()
            self._update_tags_in_qml()

    @Slot(str)
    def add_user(self, user):
        """ Ajoute un utilisateur à la liste des utilisateurs. """
        if user.strip():
            self.users.append(user)
            self._update_users_in_qml()
        else:
            print("Erreur : Utilisateur invalide.")

    @Slot()
    def remove_last_user(self):
        """ Retire le dernier utilisateur ajouté. """
        if self.users:
            self.users.pop()
            self._update_users_in_qml()

    def _update_tags_in_qml(self):
        """ Met à jour la liste des tags dans l'interface QML. """
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("tagsListModel", self.tags)

    def _update_users_in_qml(self):
        """ Met à jour la liste des utilisateurs dans l'interface QML. """
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("usersListModel", self.users)

    @Slot(str)
    def add_start_date(self, startdate):
        """ Définit la date de début de la tâche après validation. """
        try:
            self.start_date = self._validate_date_format(startdate)
        except ValueError as e:
            print(f"Erreur : {e}")

    @Slot(str)
    def add_end_date(self, enddate):
        """ Définit la date de fin de la tâche après validation. """
        try:
            self.end_date = self._validate_date_format(enddate)
        except ValueError as e:
            print(f"Erreur : {e}")

    def _validate_date_format(self, date_str):
        """
        Valide le format de la date (jj/mm/aaaa).
        Retourne une date formatée en 'aaaa-mm-jj' pour la base de données.
        """
        try:
            return datetime.strptime(date_str, "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")
        except ValueError:
            raise ValueError(f"Format de date invalide : {date_str}. Utilisez le format jj/mm/aaaa.")

    def _check_dates_consistency(self):
        """ Vérifie que la date de début est antérieure à la date de fin. """
        if self.start_date and self.end_date:
            start = datetime.strptime(self.start_date, "%Y-%m-%d 00:00:00")
            end = datetime.strptime(self.end_date, "%Y-%m-%d 00:00:00")
            if start > end:
                raise ValueError("La date de début ne peut pas être postérieure à la date de fin.")

    @Slot()
    def validate_info(self):
        """
        Valide les informations de la tâche, en vérifiant les entrées
        avant de les insérer dans la base de données.
        """
        try:
            if not self.task_name:
                raise ValueError("Le nom de la tâche ne peut pas être vide.")

            if not self.start_date or not self.end_date:
                raise ValueError("Les dates de début et de fin doivent être renseignées.")

            self._check_dates_consistency()

            formatted_tags = ", ".join(self.tags)

            # Insérer la tâche dans la base de données
            insert_task("Task", {
                "name": self.task_name,
                "end_date": self.end_date,
                "checked": "0",
                "priority": self.task_priority,
                "tag": formatted_tags,
            })

            # Afficher les informations de la tâche pour débogage
            print("----- Informations sur la tâche -----")
            priority_labels = ["Priorité basse", "Priorité moyenne", "URGENT"]
            print(f"Nom de la tâche : {self.task_name}")
            print(f"Priorité : {priority_labels[self.task_priority]}")
            print(f"Tags : {self.tags}")
            print(f"Utilisateurs : {self.users}")
            print(f"Date de début : {self.start_date}")
            print(f"Date de fin : {self.end_date}")

        except ValueError as e:
            print(f"Erreur de validation : {e}")


if __name__ == '__main__':
    # Création de l'application et chargement du moteur QML
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Définir le répertoire de l'application
    app_dir = Path(__file__).parent.parent

    # Ajout des chemins d'importation pour QML
    engine.addImportPath(os.fspath(app_dir))
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    # Instanciation du gestionnaire de tâches et connexion avec QML
    task_handler = TaskHandler(engine)
    engine.rootContext().setContextProperty("taskHandler", task_handler)

    # Chargement du fichier QML principal
    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
