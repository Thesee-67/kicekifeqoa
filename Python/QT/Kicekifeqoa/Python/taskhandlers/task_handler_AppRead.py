from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Read_Task import get_data
from Python.CRUD.Subtask.Read_Subtask import get_data as get_subtask_data
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format

class TaskHandler(QObject):
    # Signaux pour chaque colonne
    tasksFetchedPriority2 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority1 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority0 = Signal(list, arguments=['tasks'])
    tasksFetchedChecked = Signal(list, arguments=['tasks'])

    @Slot()
    def fetchTasks(self):
        # Récupérer les tâches principales et les sous-tâches
        tasks_priority2 = self.get_tasks_from_api(priority_filter=2, exclude_checked=True)
        tasks_priority1 = self.get_tasks_from_api(priority_filter=1, exclude_checked=True)
        tasks_priority0 = self.get_tasks_from_api(priority_filter=0, exclude_checked=True)
        tasks_checked = self.get_tasks_from_api(checked_filter=1)
        subtasks = self.get_subtasks_from_api(exclude_checked=True)

        # Grouper les sous-tâches avec leurs tâches parentes
        grouped_priority2 = self.group_tasks_with_subtasks(tasks_priority2, subtasks)
        grouped_priority1 = self.group_tasks_with_subtasks(tasks_priority1, subtasks)
        grouped_priority0 = self.group_tasks_with_subtasks(tasks_priority0, subtasks)
        grouped_checked = self.group_tasks_with_subtasks(tasks_checked, subtasks)

        # Émettre les tâches groupées
        self.tasksFetchedPriority2.emit(grouped_priority2)
        self.tasksFetchedPriority1.emit(grouped_priority1)
        self.tasksFetchedPriority0.emit(grouped_priority0)
        self.tasksFetchedChecked.emit(grouped_checked)

    def get_tasks_from_api(self, priority_filter=None, checked_filter=None, exclude_checked=False):
        # Appel à l'API pour récupérer toutes les tâches principales
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

            return [{
                "id_task": task['id_task'],
                "name": task['name'],
                "end_date": read_date_format(task['end_date']),
                "checked": task['checked'],
                "priority": task['priority'],
                "tag": task['tag']
            } for task in filtered_tasks]

    def get_subtasks_from_api(self, exclude_checked=False):
        # Appel à l'API pour récupérer les sous-tâches
        subtasks_response = get_subtask_data("Subtask", columns="id_subtask, id_affected_task, name, end_date, checked")
        tasks_response = get_data("Task", columns="id_task, priority")

        if isinstance(subtasks_response, str) and subtasks_response.startswith("Erreur"):
            print(f"Erreur lors de la récupération des sous-tâches : {subtasks_response}")
            return []
        if isinstance(tasks_response, str) and tasks_response.startswith("Erreur"):
            print(f"Erreur lors de la récupération des tâches parentes : {tasks_response}")
            return []

        # Créer un dictionnaire pour les priorités des tâches parentes
        task_priorities = {task['id_task']: task['priority'] for task in tasks_response}

        filtered_subtasks = subtasks_response

        # Exclure les sous-tâches cochées si demandé
        if exclude_checked:
            filtered_subtasks = [subtask for subtask in filtered_subtasks if subtask['checked'] != 1]

        # Formater les sous-tâches pour qu'elles ressemblent aux tâches principales et héritent de la priorité de la tâche parente
        return [{
            "id_task": float(f"{subtask['id_subtask']}.{subtask['id_affected_task']}"),
            "id_task_str": f"{subtask['id_subtask']}.{subtask['id_affected_task']}",
            "name": f"↳ {subtask['name']}",
            "end_date": read_date_format(subtask['end_date']),
            "checked": subtask['checked'],
            "priority": task_priorities.get(subtask['id_affected_task'], None),
            "tag": "",
            "parent_id": subtask['id_affected_task']
        } for subtask in filtered_subtasks]

    def group_tasks_with_subtasks(self, tasks, subtasks):
        # Dictionnaire pour grouper les sous-tâches par ID de tâche parente
        subtasks_by_parent = {}
        for subtask in subtasks:
            parent_id = subtask['parent_id']
            if parent_id not in subtasks_by_parent:
                subtasks_by_parent[parent_id] = []
            subtasks_by_parent[parent_id].append(subtask)

        # Liste pour stocker les tâches principales avec leurs sous-tâches associées
        grouped_tasks = []
        for task in tasks:
            grouped_tasks.append(task)
            if task['id_task'] in subtasks_by_parent:
                grouped_tasks.extend(subtasks_by_parent[task['id_task']])

        return grouped_tasks
