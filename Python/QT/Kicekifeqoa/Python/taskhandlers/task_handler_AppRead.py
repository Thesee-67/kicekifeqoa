from PySide6.QtCore import QObject, Slot, Signal
from Python.CRUD.Task.Read_Task import get_data
from Python.CRUD.Subtask.Read_Subtask import get_data as get_subtask_data
from Python.QT.Kicekifeqoa.Python.format_date import read_date_format


class TaskHandler(QObject):
    tasksFetchedPriority2 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority1 = Signal(list, arguments=['tasks'])
    tasksFetchedPriority0 = Signal(list, arguments=['tasks'])
    tasksFetchedChecked = Signal(list, arguments=['tasks'])  # 4e colonne pour les tâches cochées

    @Slot()
    def fetchTasksAndSubtasksByPriority(self, priority):
        """
        Fetches tasks and subtasks grouped by priority and combines them
        so that subtasks appear under their parent tasks.
        """
        # Fetch tasks and subtasks
        tasks = self.get_tasks_from_api(priority_filter=priority, exclude_checked=True)
        subtasks = self.get_subtasks_from_api(exclude_checked=True)

        combined_tasks = []

        for task in tasks:
            # Add the main task
            task_with_subtasks = {
                "id_task": task['id_task'],
                "name": task['name'],
                "end_date": task['end_date'],
                "checked": task['checked'],
                "priority": task['priority'],
                "tag": task['tag'],
                "type": "task",  # Main task indicator
                "subtasks": []  # Initialize subtasks list
            }

            # Add the subtasks corresponding to this task
            for subtask in subtasks:
                if subtask['id_affected_task'] == task['id_task']:
                    task_with_subtasks["subtasks"].append({
                        "id_subtask": subtask['id_subtask'],
                        "name": subtask['name'],
                        "end_date": subtask['end_date'],
                        "checked": subtask['checked'],
                        "type": "subtask"  # Subtask indicator
                    })

            combined_tasks.append(task_with_subtasks)

        # Emit the combined data based on priority
        if priority == 2:
            self.tasksFetchedPriority2.emit(combined_tasks)
        elif priority == 1:
            self.tasksFetchedPriority1.emit(combined_tasks)
        elif priority == 0:
            self.tasksFetchedPriority0.emit(combined_tasks)

    @Slot()
    def fetchCheckedTasks(self):
        """
        Fetches only the checked tasks (main tasks with checked = 1).
        """
        tasks = self.get_tasks_from_api(checked_filter=1)
        # No subtasks are included for this column
        checked_tasks = [
            {
                "id_task": task['id_task'],
                "name": task['name'],
                "end_date": task['end_date'],
                "checked": task['checked'],
                "priority": task['priority'],
                "tag": task['tag'],
                "type": "task"  # Main task indicator
            }
            for task in tasks
        ]

        self.tasksFetchedChecked.emit(checked_tasks)

    @Slot()
    def fetchTasks(self):
        """
        Fetches and emits tasks and subtasks for all priorities and checked tasks.
        """
        self.fetchTasksAndSubtasksByPriority(2)
        self.fetchTasksAndSubtasksByPriority(1)
        self.fetchTasksAndSubtasksByPriority(0)
        self.fetchCheckedTasks()  # Fetch the checked tasks for the 4th column

    def get_tasks_from_api(self, priority_filter=None, checked_filter=None, exclude_checked=False):
        """
        Fetches tasks from the API and filters them based on priority or checked status.
        """
        response = get_data("Task", columns="id_task, name, end_date, checked, priority, tag")

        if isinstance(response, str) and response.startswith("Erreur"):
            print(f"Erreur lors de la récupération des tâches : {response}")
            return []
        else:
            filtered_tasks = response

            # Filter by priority if applicable
            if priority_filter is not None:
                filtered_tasks = [task for task in filtered_tasks if task['priority'] == priority_filter]

            # Exclude checked tasks if requested
            if exclude_checked:
                filtered_tasks = [task for task in filtered_tasks if task['checked'] != 1]

            # Filter by checked status if applicable
            if checked_filter is not None:
                filtered_tasks = [task for task in filtered_tasks if task['checked'] == checked_filter]

            # Format the date before returning the tasks
            return [{"id_task": task['id_task'],
                     "name": task['name'],
                     "end_date": read_date_format(task['end_date']),
                     "checked": task['checked'],
                     "priority": task['priority'],
                     "tag": task['tag']}
                    for task in filtered_tasks]

    def get_subtasks_from_api(self, checked_filter=None, exclude_checked=False):
        """
        Fetches subtasks from the API and filters them based on checked status.
        """
        response = get_subtask_data("Subtask", columns="id_subtask, id_affected_task, name, end_date, checked")

        if isinstance(response, str) and response.startswith("Erreur"):
            print(f"Erreur lors de la récupération des sous-tâches : {response}")
            return []
        else:
            filtered_subtasks = response

            # Exclude checked subtasks if requested
            if exclude_checked:
                filtered_subtasks = [subtask for subtask in filtered_subtasks if subtask['checked'] != 1]

            # Filter by checked status if applicable
            if checked_filter is not None:
                filtered_subtasks = [subtask for subtask in filtered_subtasks if subtask['checked'] == checked_filter]

            # Format the date before returning the subtasks
            return [{"id_subtask": subtask['id_subtask'],
                     "id_affected_task": subtask['id_affected_task'],
                     "name": subtask['name'],
                     "end_date": read_date_format(subtask['end_date']),
                     "checked": subtask['checked']}
                    for subtask in filtered_subtasks]
