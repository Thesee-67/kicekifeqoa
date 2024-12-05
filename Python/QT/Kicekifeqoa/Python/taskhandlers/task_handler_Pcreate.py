from PySide6.QtCore import QObject, Slot
from Python.CRUD.Task.Create_Task import create_task
from Python.CRUD.Task.Read_Task import add_recup
from Python.CRUD.Task_has_Users.Create_Task_has_Users import create_task_user_association

class TaskHandler(QObject):
    def __init__(self, engine, TaskHandlerLogin):
        super().__init__()
        self.engine = engine
        self.login_handler = TaskHandlerLogin
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.users = []
        self.end_date = None
        self.checked = 0
        self.user_id = None

    @Slot(str)
    def add_task_name(self, taskname):
        if taskname.strip():
            self.task_name = taskname
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

    @Slot(int)
    def add_task_priority(self, priority):
        if priority in [0, 1, 2]:
            self.task_priority = priority
        else:
            print("Erreur : Priorité invalide.")

    @Slot(str)
    def add_tag(self, tag):
        if tag.strip():
            self.tags.append(tag)
            self._update_tags_in_qml()
        else:
            print("Erreur : Tag invalide.")

    @Slot()
    def remove_last_tag(self):
        if self.tags:
            self.tags.pop()
            self._update_tags_in_qml()

    @Slot(str)
    def add_user(self, user):
        if user.strip():
            self.users.append(user)
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
    def add_end_date(self, enddate):
        try:
            self.end_date = self._validate_date_format(enddate)
        except ValueError as e:
            print(f"Erreur : {e}")

    def _validate_date_format(self, date_str):
        from Python.QT.Kicekifeqoa.Python.format_date import validate_date_format
        return validate_date_format(date_str)

    def _check_dates_consistency(self):
        if self.end_date:
            from Python.QT.Kicekifeqoa.Python.format_date import check_dates_consistency
            check_dates_consistency(self.end_date)

    @Slot(int)
    def task_completed(self, status):
        self.checked = status

    @Slot()
    def validate_info(self):
        try:
            # Récupérer l'ID utilisateur depuis le login_handler
            self.user_id = self.login_handler.get_user_id()
            print(self.user_id)

            if not self.task_name:
                raise ValueError("Le nom de la tâche ne peut pas être vide.")
            if not self.end_date:
                raise ValueError("La date de fin doit être renseignée.")
            self._check_dates_consistency()
            formatted_tags = ", ".join(self.tags)

            create_task("Task", {
                "name": self.task_name,
                "end_date": self.end_date,
                "checked": self.checked,
                "priority": self.task_priority,
                "tag": formatted_tags,
            })

            data = {"Task": {"name": self.task_name, "end_date": self.end_date, "checked": self.checked, "priority": self.task_priority, "tag": formatted_tags}}
            id_task = add_recup(data)

            # Associer l'utilisateur à cette tâche dans la table Task_has_Users
            create_task_user_association("Task_has_Users", {
                "task_id": id_task,
                "user_id": self.user_id,
            })


            self.task_name = ""
            self.task_priority = 0
            self.tags = []
            self.users = []
            self.end_date = None
            self.checked = 0

        except ValueError as e:
            print(f"Erreur de validation : {e}")
