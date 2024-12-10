from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Read_Task import get_data
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format

class TaskHandlerAppRead(QObject):
    tasksFetchedPriority2 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority1 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority0 = Signal(list, arguments=['tasks'])
    tasksFetchedChecked = Signal(list, arguments=['tasks'])  # Nouveau signal pour les tâches cochées

    def __init__(self, engine):
        super(TaskHandlerAppRead, self).__init__()
        self.engine = engine

    @Slot(int)
    def fetchTasks(self, user_id):
        tasks =  self.get_tasks_from_api(user_id=user_id)

        # Créer des listes pour chaque catégorie
        tasks_priority2 = []
        tasks_priority1 = []
        tasks_priority0 = []
        tasks_checked = []

        # Trier les tâches en fonction de leur priorité et statut
        for task in tasks:
            if task['checked'] == 1:
                tasks_checked.append(task)
            elif task['priority'] == 2:
                tasks_priority2.append(task)
            elif task['priority'] == 1:
                tasks_priority1.append(task)
            elif task['priority'] == 0:
                tasks_priority0.append(task)

        # Émettre les tâches groupées
        self.tasksFetchedPriority2.emit(tasks_priority2)
        self.tasksFetchedPriority1.emit(tasks_priority1)
        self.tasksFetchedPriority0.emit(tasks_priority0)
        self.tasksFetchedChecked.emit(tasks_checked)

    def get_tasks_from_api(self, user_id=None, priority_filter=None, checked_filter=None, exclude_checked=False):

        response = get_data(
            "Task_has_Users",
            columns="Task.*",  # Récupérer toutes les colonnes de Task
            join_table="Task",  # Joindre uniquement la table Task
            join_condition="Task_has_Users.task_id = Task.id_task",
            filter_column="Task_has_Users.user_id",  # Filtrer par l'ID utilisateur dans Task_has_Users
            filter_value=user_id  # ID de l'utilisateur authentifié
        )

        if isinstance(response, str) and response.startswith("Erreur"):
            print(f"Erreur lors de la récupération des tâches : {response}")
            return []
        else:
            filtered_tasks = response

            # Filtrer par priorité si applicable
            if priority_filter is not None:
                filtered_tasks = [task for task in filtered_tasks if task['priority'] == priority_filter]

            # Exclure les tâches cochées si demandé
            if exclude_checked:
                filtered_tasks = [task for task in filtered_tasks if task['checked'] != 1]

            # Filtrer par tâches cochées si applicable
            if checked_filter is not None:
                filtered_tasks = [task for task in filtered_tasks if task['checked'] == checked_filter]

            # Conversion de la date au format DD/MM/YYYY avant de renvoyer les tâches
            return [{"id_task": task['id_task'],
                     "name": task['name'],
                     "end_date": read_date_format(task['end_date']),
                     "checked": task['checked'],
                     "priority": task['priority'],
                     "tag": task['tag']}
                    for task in filtered_tasks]

