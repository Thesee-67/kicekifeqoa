import sys
from PySide6.QtCore import QUrl, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class TaskHandler(QObject):
    def __init__(self):
        super().__init__()
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.users = []

    @Slot(str)
    def update_task_name(self, name):
        self.task_name = name

    @Slot(int)
    def update_task_priority(self, priority):
        self.task_priority = priority

    @Slot(str)
    def add_tag(self, tag):
        self.tags.append(tag)
        self.update_tags_in_qml()

    @Slot()
    def remove_last_tag(self):
        if self.tags:
            self.tags.pop()
        self.update_tags_in_qml()

    @Slot(str)
    def add_user(self, email):
        self.users.append(email)
        self.update_users_in_qml()

    @Slot()
    def remove_last_user(self):
        if self.users:
            self.users.pop()
        self.update_users_in_qml()

    def update_tags_in_qml(self):
        root_object = engine.rootObjects()[0]
        root_object.setProperty("tagsListModel", self.tags)

    def update_users_in_qml(self):
        root_object = engine.rootObjects()[0]
        root_object.setProperty("usersListModel", self.users)

    @Slot()
    def print_all_info(self):
        print("----- Task Information -----")
        print(f"Task - name: {self.task_name}")
        priority_labels = ["Priorité basse", "Priorité moyenne", "URGENT"]
        print(f"Task - priority: {self.task_priority}")
        print(f"Tags: {self.tags}")
        print(f"Users: {self.users}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    qml_file = QUrl("App.qml")
    engine.load(qml_file)

    if not engine.rootObjects():
        print("Erreur : Impossible de charger le fichier QML.")
        sys.exit(-1)

    task_handler = TaskHandler()

    root_object = engine.rootObjects()[0]

    # Connecter les signaux QML aux slots Python
    root_object.updateTaskName.connect(task_handler.update_task_name)
    root_object.updateTaskPriority.connect(task_handler.update_task_priority)
    root_object.addTag.connect(task_handler.add_tag)
    root_object.removeLastTag.connect(task_handler.remove_last_tag)
    root_object.addUser.connect(task_handler.add_user)
    root_object.removeLastUser.connect(task_handler.remove_last_user)
    root_object.printAllInfo.connect(task_handler.print_all_info)

    sys.exit(app.exec())