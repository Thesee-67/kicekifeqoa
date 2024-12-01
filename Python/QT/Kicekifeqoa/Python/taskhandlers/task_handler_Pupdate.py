from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Update_Task import update_task, fetch_task
from Python.CRUD.Task.Read_Task import get_task
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format
import requests

class TaskHandler(QObject):
    taskFetched = Signal(dict)  # Signal pour transmettre les données au QML

    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_id = ""
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.end_date = None
        self.checked = 0

    @Slot(str)
    def fetch_task_by_id(self, task_id):
        try:
            print(f"Fetching task with ID: {task_id}")
            task_data = get_task(id_task=task_id)
            print(f"Data received: {task_data}")

            if isinstance(task_data, list) and len(task_data) > 0:
                task = task_data[0]
                print(f"Task found: {task}")
                self.task_id = task_id
                self.task_name = task.get("name", "")
                self.task_priority = task.get("priority", 0)
                self.tags = task.get("tag", "").split(",") if task.get("tag") else []

                # Formater la date de fin avant de l'assigner
                raw_end_date = task.get("end_date", None)
                if raw_end_date:
                    self.end_date = read_date_format(raw_end_date)  # Formater au format 'dd/mm/yyyy'
                else:
                    self.end_date = None

                self.checked = task.get("checked", 0)

                # Créer un dictionnaire avec toutes les données et émettre vers QML
                task_info = {
                    "task_id": self.task_id,
                    "task_name": self.task_name,
                    "task_priority": self.task_priority,
                    "tags": self.tags,
                    "end_date": self.end_date,  # La date formatée
                    "checked": self.checked
                }

                # Émettre le dictionnaire formaté
                self.taskFetched.emit(task_info)

            else:
                print(f"Aucune tâche trouvée avec l'ID : {task_id}")
        except Exception as e:
            print(f"Erreur lors de la récupération de la tâche : {e}")

    @Slot(str)
    def update_task_name(self, updatetaskname):
        if updatetaskname.strip():
            self.task_name = updatetaskname
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

    @Slot(int)
    def update_task_priority(self, updatepriority):
        if updatepriority in [0, 1, 2]:
            self.task_priority = updatepriority
        else:
            print("Erreur : Priorité invalide.")

    @Slot(str)
    def add_tag(self, tagname):
        if tagname.strip():
            self.tags.append(tagname)
            self._update_tags_in_qml()
        else:
            print("Erreur : Tag invalide.")

    @Slot()
    def remove_last_tag(self):
        if self.tags:
            self.tags.pop()
            self._update_tags_in_qml()

    @Slot(str)
    def add_user(self, username):
        if username.strip():
            self.users.append(username)
            self._update_users_in_qml()
        else:
            print("Erreur : Utilisateur invalide.")

    @Slot()
    def remove_last_user(self):
        if self.users:
            self.users.pop()
            self._update_users_in_qml()

    def _update_tags_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("tagsListModel", self.tags)

    def _update_users_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("usersListModel", self.users)

    @Slot(str)
    def update_end_date(self, updateenddate):
        try:
            self.end_date = self._validate_date_format(updateenddate)
        except ValueError as e:
            print(f"Erreur : {e}")

    def _validate_date_format(self, date_str):
        from Python.QT.Kicekifeqoa.Python.format_date import validate_date_format
        return validate_date_format(date_str)


    @Slot(int)
    def task_completed(self, status):
        self.checked = status

    @Slot()
    def validate_update_info(self):
        try:
            if not self.task_name.strip():
                raise ValueError("Le nom de la tâche est obligatoire.")
            if not self.end_date.strip():
                raise ValueError("La date de fin est obligatoire.")

            response = update_task(
                id_task=self.task_id,
                name=self.task_name,
                end_date=self.end_date,
                checked=self.checked,
                priority=self.task_priority,
                tag=", ".join(self.tags)
            )

            if "succès" in response.lower():
                print("Mise à jour réussie :", response)
            else:
                print("Erreur lors de la mise à jour :", response)
        except ValueError as ve:
            print("Erreur de validation :", ve)
        except Exception as e:
            print("Erreur inattendue :", e)
