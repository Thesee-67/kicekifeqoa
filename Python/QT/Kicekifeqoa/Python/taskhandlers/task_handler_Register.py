from pathlib import Path
from PySide6.QtCore import QObject, Slot, Signal
import os
from Python.CRUD.Users.Read_User import  get_data
from Python.CRUD.Users.Create_User import create_user

class TaskHandler(QObject):
     alreadymail = Signal()  # Déclaration du signal

    def __init__(self, engine):
        super(TaskHandler, self).__init__()
        self.engine = engine

    @Slot(str, str)
    def checkCredentials(self, email):
        result = get_data(
            table="Users",
            filter_column="email",
            filter_value=email,
        )

        if result and isinstance(result, list) and len(result) > 0:
            user_data = result[0]

            if user_data.get('email') == email:
                self.alreadymail.emit()
            else:
                post_data = {
                    'table': table,
                    'action': 'insert',
                    'data': data
                }
                response = requests.post(url, json=post_data)

