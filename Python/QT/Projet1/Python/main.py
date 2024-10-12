import os
import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl, QObject, Signal, Slot

from Python.CRUD.Subtask.Create import end_date
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
    def add_task_name(self, taskname):
        self.task_name = taskname

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
    def add_user(self, user):
        self.users.append(user)
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

    @Slot(str)
    def add_start_date(self, startdate):
        self.start_date = startdate

    @Slot(str)
    def add_end_date(self, enddate):
        self.end_date = enddate

    @Slot()
    def validate_info(self):
        formatted_tags = ", ".join(self.tags)
        formatted_startdate = datetime.strptime(self.start_date, "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")
        formatted_enddate = datetime.strptime(self.end_date, "%d/%m/%Y").strftime("%Y-%m-%d 00:00:00")

        insert_task("Task", {
            "name": self.task_name,
            "end_date": formatted_enddate,
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
        print(f"StartDate: {formatted_startdate}")
        print(f"EndDate: {formatted_enddate}")



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