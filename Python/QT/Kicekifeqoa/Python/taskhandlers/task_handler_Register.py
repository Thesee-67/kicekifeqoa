from pathlib import Path
from PySide6.QtCore import QObject, Slot, Signal
import os
from Python.CRUD.Users.Read_User import get_data
from Python.CRUD.Users.Create_User import create_user

class TaskHandler(QObject):
    alreadyMail = Signal()  # Déclaration du signal
    registerSuccess = Signal()  # Déclaration du signal

    def __init__(self, engine):
        super(TaskHandler, self).__init__()
        self.engine = engine

    @Slot(str, str)  # Accepter deux paramètres : email et password
    def checkCredentials(self, email, password):
        result = get_data(
            table="Users",
            filter_column="email",
            filter_value=email,
        )

        if result and isinstance(result, list) and len(result) > 0:
            user_data = result[0]

            if user_data.get('email') == email:
                self.alreadyMail.emit()  # Émettre le signal si l'email existe déjà
        else:
            # Si l'utilisateur n'existe pas, on peut ajouter un nouvel utilisateur
            self.add_user(email, password)  # Ajout de l'utilisateur
            self.registerSuccess.emit()

    def add_user(self, email, password):
        create_user("Users", {
            "email": email,
            "password": password,
        })
