from pathlib import Path
from PySide6.QtCore import QObject, Slot, Signal
import os
from Python.CRUD.Users.Read_User import  get_users
import bcrypt

class TaskHandler(QObject):
    loginSuccess = Signal()  # Déclaration du signal
    loginPasswdFail = Signal()
    loginEmailFail = Signal()

    def __init__(self, engine):
        super(TaskHandler, self).__init__()
        self.engine = engine

    def verify_password(self,stored_password,provided_password):
        # Compare le mot de passe fourni avec le hash stocké
        password = bcrypt.checkpw(provided_password.encode(),stored_password)
        return password

    @Slot(str, str)
    def checkCredentials(self, email, password):
        if email != "": # Vérifie si le mail n'est pas vide
            result = get_users(email=email)
        else:
            result = 'no existing links'

        if result != 'no existing links':
            user_data = result[0]
            stored_password = (user_data.get("password")).encode("utf-8") #transforme le hash de str a Bytes

            if self.verify_password(stored_password,password):
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