from PySide6.QtCore import QObject, Slot
from Python.CRUD.Task.Delete import delete_task

class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_name = ""
        self.delete_info = ""


    @Slot()
    def validate_delete_info(self):
        try:
            if not self.delete_info:
                raise ValueError("Aucune tache n'est selectionnée")

            #delete_task("Task", "name", {self.task_name})

            print(f"Deleted : {self.task_name}")

        except ValueError as e:
            print(f"Erreur de validation : {e}")
