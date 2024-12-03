from PySide6.QtCore import QObject, Slot
from Python.CRUD.Subtask.Create_Subtask import create_subtask

class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_id = ""
        self.task_name = ""
        self.end_date = None
        self.checked = 0

    @Slot(str)
    def parent_task_id(self, parenttaskid):
        if parenttaskid.strip():
            self.parent_task_id = parenttaskid
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

    @Slot(str)
    def add_task_name(self, taskname):
        if taskname.strip():
            self.task_name = taskname
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

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
        print("CEST BON")
        print(self.task_name)
        print(self.end_date)
        print(self.checked)
        print(self.parent_task_id)

        try:
            if not self.task_name:
                raise ValueError("Le nom de la tâche ne peut pas être vide.")
            if not self.end_date:
                raise ValueError("La date de fin doit être renseignée.")
            self._check_dates_consistency()

            create_subtask("Subtask", {
                "id_affected_task": self.parent_task_id,
                "name": self.task_name,
                "end_date": self.end_date,
                "checked": self.checked,
            })

        except ValueError as e:
            print(f"Erreur de validation : {e}")