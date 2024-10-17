from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Read import get_data
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format

class TaskHandler(QObject):
    # Signal pour renvoyer la liste des tâches vers QML
    tasksFetched = Signal(list, arguments=['tasks'])

    @Slot()
    def fetchTasks(self):
        # Appel de la méthode get_data pour récupérer les tâches depuis l'API
        tasks = self.get_tasks_from_api()
        self.tasksFetched.emit(tasks)

    def get_tasks_from_api(self):
        # Appel à l'API pour récupérer toutes les tâches
        response = get_data("Task", columns="id_task, name, end_date, checked, priority, tag")

        if isinstance(response, str) and response.startswith("Erreur"):
            # Gestion des erreurs si la requête échoue
            print(f"Erreur lors de la récupération des tâches : {response}")
            return []
        else:
            # Conversion de la date au format DD/MM/YYYY avant de renvoyer les tâches
            return [{"id_task": task['id_task'],
                     "name": task['name'],
                     "end_date": read_date_format(task['end_date']),  # Utilisation de format_date importée
                     "checked": task['checked'],
                     "priority": task['priority'],
                     "tag": task['tag']}
                    for task in response]
