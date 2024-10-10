import sys
from PySide6.QtCore import QUrl, QObject, Signal, Slot
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

class TaskHandler(QObject):
    def __init__(self):
        super().__init__()

    @Slot(str)
    def task_name(self, name):
        print(f"Task - name: {name}")

    @Slot(int)
    def task_priority(self, priority):
        print(f"Task - priority: {priority}")

    @Slot(str)
    def add_tag(self, tag):
        print(f"Task - tag added: {tag}")

    @Slot(str)
    def remove_tag(self, tag):
        print(f"Task - tag removed: {tag}")

    @Slot(str)
    def add_user(self, email):
        print(f"Task_has_Users - added user: {email}")

    @Slot(str)
    def remove_user(self, email):
        print(f"Task_has_Users - removed user: {email}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Charger le fichier QML
    qml_file = QUrl("App.qml")
    engine.load(qml_file)

    if not engine.rootObjects():
        print("Erreur : Impossible de charger le fichier QML.")
        sys.exit(-1)

    task_handler = TaskHandler()

    # Connecter les signaux QML aux slots Python
    root_object = engine.rootObjects()[0]

    root_object.taskName.connect(task_handler.task_name)
    root_object.taskPriority.connect(task_handler.task_priority)
    root_object.addTag.connect(task_handler.add_tag)
    root_object.removeTag.connect(task_handler.remove_tag)
    root_object.addUser.connect(task_handler.add_user)
    root_object.removeUser.connect(task_handler.remove_user)

    sys.exit(app.exec())
