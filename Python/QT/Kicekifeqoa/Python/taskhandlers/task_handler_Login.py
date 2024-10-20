from pathlib import Path
from PySide6.QtCore import QObject, Slot
import os
from Python.CRUD.Users.Read_User import  get_data

class TaskHandler(QObject):
    def __init__(self, engine):
        super(TaskHandler, self).__init__()
        self.engine = engine

    @Slot(str, str)
    def checkCredentials(self, email, password):
        # Utiliser les deux filtres dans la requête API
        result = get_data(
            table="Users",
            filter_column="email",
            filter_value=email,
            filter_column2="password",
            filter_value2=password
        )

        # Vérifier si result est une liste et contient au moins un élément
        if result and isinstance(result, list) and len(result) > 0:
            # Accéder au premier élément de la liste (données utilisateur)
            user_data = result[0]

            # Vérifier le mot de passe (s'il est renvoyé par l'API)
            if user_data.get('password') == password:
                # Charger la nouvelle interface App.qml
                app_qml_path = os.path.join(os.path.dirname(__file__), "..", "KicekifeqoaContent", "App.qml")
                self.engine.load(os.fspath(Path(app_qml_path).resolve()))  # Utilisation du chemin relatif
            else:
                print("Mot de passe incorrect")
        else:
            print("Utilisateur non trouvé ou informations incorrectes.")


