from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Read_Task import get_data
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format

class TaskHandler(QObject):
    tasksFetchedPriority2 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority1 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority0 = Signal(list, arguments=['tasks'])
    tasksFetchedChecked = Signal(list, arguments=['tasks'])  # Nouveau signal pour les tâches cochées

    @Slot()
    def fetchTasks(self):
        # Appelle les trois fonctions pour chaque priorité
        self.fetchTasksPriority2()
        self.fetchTasksPriority1()
        self.fetchTasksPriority0()
        self.fetchTasksChecked()  # Appel de la nouvelle fonction pour les tâches cochées

    @Slot()
    def fetchTasksPriority2(self):
        tasks = self.get_tasks_from_api(priority_filter=2, exclude_checked=True)
        self.tasksFetchedPriority2.emit(tasks)

    @Slot()
    def fetchTasksPriority1(self):
        tasks = self.get_tasks_from_api(priority_filter=1, exclude_checked=True)
        self.tasksFetchedPriority1.emit(tasks)

    @Slot()
    def fetchTasksPriority0(self):
        tasks = self.get_tasks_from_api(priority_filter=0, exclude_checked=True)
        self.tasksFetchedPriority0.emit(tasks)

    @Slot()
    def fetchTasksChecked(self):
        tasks = self.get_tasks_from_api(checked_filter=1)
        self.tasksFetchedChecked.emit(tasks)

    def get_tasks_from_api(self, priority_filter=None, checked_filter=None, exclude_checked=False):
        # Appel à l'API pour récupérer toutes les tâches
        response = get_data("Task", columns="id_task, name, end_date, checked, priority, tag")

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
