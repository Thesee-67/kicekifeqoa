from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Subtask.Update_Subtask import update_subtask
from Python.CRUD.Subtask.Read_Subtask import get_subtask
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format

class TaskHandler(QObject):
    taskFetched = Signal(dict)

    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_id = ""
        self.parent_task_id = ""
        self.task_name = ""
        self.end_date = None
        self.checked = 0

    @Slot(str)
    def fetch_task_by_id(self, task_id):
        try:
            task_data = get_subtask(id_subtask=task_id)

            if isinstance(task_data, list) and len(task_data) > 0:
                task = task_data[0]
                self.task_id = task_id
                self.parent_task_id = task.get("id_affected_task", "")
                self.task_name = task.get("name", "")
                raw_end_date = task.get("end_date", None)

                if raw_end_date:
                    self.end_date = read_date_format(raw_end_date)
                else:
                    self.end_date = None
                self.checked = task.get("checked", 0)

                task_info = {
                    "task_id": self.task_id,
                    "parent_task_id": self.parent_task_id,
                    "task_name": self.task_name,
                    "end_date": self.end_date,
                    "checked": self.checked
                }

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

    @Slot(str)
    def update_end_date(self, updateenddate):
        try:
            self.end_date = self._validate_date_format(updateenddate)
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
    def validate_update_info(self):
        try:
            if not self.task_name.strip():
                raise ValueError("Le nom de la tâche est obligatoire.")
            if not self.end_date.strip():
                raise ValueError("La date de fin est obligatoire.")

            response = update_subtask(
                id_subtask=self.task_id,
                id_affected_task=self.parent_task_id,
                name=self.task_name,
                end_date=self.end_date,
                checked=self.checked,
            )

            if "succès" in response.lower():
                print("Mise à jour réussie :", response)
            else:
                print("Erreur lors de la mise à jour :", response)
        except ValueError as ve:
            print("Erreur de validation :", ve)
        except Exception as e:
            print("Erreur inattendue :", e)
