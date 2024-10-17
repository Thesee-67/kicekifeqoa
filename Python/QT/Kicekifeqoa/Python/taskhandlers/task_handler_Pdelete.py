from PySide6.QtCore import QObject, Slot
from Python.CRUD.Task.Delete import delete_task

class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_name = ""
        self.delete_info = ""

    @Slot(str)
    def set_task_name(self, taskname):
        if taskname.strip():
            self.task_name = taskname
            print(self.task_name)
        else:
            print("Erreur : Le nom de la tâche ne peut pas être vide.")

    @Slot()
    def validate_delete_info(self):
        try:
            if not self.task_name:
                raise ValueError("Aucune tache n'est selectionnée")

            print(f"Table: Task, Column: name, Value: {self.task_name}")
            delete_task("Task", "name", self.task_name)

            print(f"Deleted : {self.task_name}")

        except ValueError as e:
            print(f"Erreur de validation : {e}")
