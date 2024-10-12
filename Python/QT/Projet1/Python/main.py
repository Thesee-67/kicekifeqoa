import os
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl, QObject, Signal, Slot

from autogen.settings import url, import_paths
from Python.CRUD.Task.Create import insert_task


class TaskHandler(QObject):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine
        self.task_name = ""
        self.task_priority = 0
        self.tags = []
        self.users = []

    @Slot(str)
    def add_task_name(self, name):
        self.task_name = name

    @Slot(int)
    def add_task_priority(self, priority):
        self.task_priority = priority

    @Slot(str)
    def add_tag(self, tag):
        self.tags.append(tag)
        self.add_tags_in_qml()

    @Slot()
    def remove_last_tag(self):
        if self.tags:
            self.tags.pop()
        self.add_tags_in_qml()

    @Slot(str)
    def add_user(self, email):
        self.users.append(email)
        self.add_users_in_qml()

    @Slot()
    def remove_last_user(self):
        if self.users:
            self.users.pop()
        self.add_users_in_qml()

    def add_tags_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("tagsListModel", self.tags)

    def add_users_in_qml(self):
        root_object = self.engine.rootObjects()[0]
        root_object.setProperty("usersListModel", self.users)

    @Slot()
    def validate_info(self):
        formatted_tags = ", ".join(self.tags)

        insert_task("Task", {
            "name": self.task_name,
            "end_date": "",
            "checked": "0",
            "priority": self.task_priority,
            "tag": formatted_tags,
        })

        print("----- Task Information -----")
        print(f"Task - name: {self.task_name}")
        priority_labels = ["Priorité basse", "Priorité moyenne", "URGENT"]
        print(f"Task - priority: {self.task_priority}")
        print(f"Tags: {self.tags}")
        print(f"Users: {self.users}")


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent

    engine.addImportPath(os.fspath(app_dir))
    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    task_handler = TaskHandler(engine)
    engine.rootContext().setContextProperty("taskHandler", task_handler)

    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
