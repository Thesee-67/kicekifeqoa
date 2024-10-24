from pathlib import Path
from PySide6.QtCore import QObject, Slot, Signal
import os
from Python.CRUD.Users.Read_User import  get_data

class TaskHandler(QObject):
    loginSuccess = Signal()  # Déclaration du signal
    loginPasswdFail = Signal()
    loginEmailFail = Signal()

    def __init__(self, engine):
        super(TaskHandler, self).__init__()
        self.engine = engine

    @Slot(str, str)
    def checkCredentials(self, email, password):
        result = get_data(
            table="Users",
            filter_column="email",
            filter_value=email,
            filter_column2="password",
            filter_value2=password
        )

        if result and isinstance(result, list) and len(result) > 0:
            user_data = result[0]

            if user_data.get('password') == password:
                # Émettre le signal pour fermer la fenêtre
                self.loginSuccess.emit()

                # Charger la nouvelle interface App.qml
                app_qml_path = Path(__file__).resolve().parents[2] / "KicekifeqoaContent" / "App.qml"
                print(f"Chargement de : {app_qml_path}")
                self.engine.load(os.fspath(app_qml_path))
            else:
                self.loginPasswdFail.emit()
        else:
            self.loginEmailFail.emit()