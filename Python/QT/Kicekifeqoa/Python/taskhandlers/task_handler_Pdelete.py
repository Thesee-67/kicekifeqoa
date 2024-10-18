from PySide6.QtCore import QObject, Slot
from Python.CRUD.Task.Delete import delete_task

class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_id = ""
        self.delete_info = ""

    @Slot(str)
    def set_task_id(self, taskid):
        if taskid.strip():
            self.task_id = taskid
            print(self.task_id)
        else:
            print("Erreur : L'id de la tâche ne peut pas être vide.")


    @Slot()
    def validate_delete_info(self):
        try:
            if not self.task_id:
                raise ValueError("Aucune tâche n'est sélectionnée")

            delete_task("Task", "name", self.task_id)
            print(f"Deleted : {self.task_id}")

        except ValueError as e:
            print(f"Erreur de validation : {e}")

