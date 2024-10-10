import sys
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

# Fonction appelée lorsque le bouton est pressé
def button_pressed():
    print("Hello, World!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Créer le moteur QML
    engine = QQmlApplicationEngine()

    # Charger le fichier QML
    qml_file = QUrl("App.qml")
    engine.load(qml_file)

    # Vérifier si le fichier QML a été chargé correctement
    if not engine.rootObjects():
        print("Erreur : Impossible de charger le fichier QML.")
        sys.exit(-1)

    # Obtenir l'objet racine de l'application QML
    root_object = engine.rootObjects()[0]

    # Connexion du signal 'buttonPressed' au slot Python 'button_pressed'
    if hasattr(root_object, "buttonPressed"):
        root_object.buttonPressed.connect(button_pressed)
        print("Connexion au signal 'buttonPressed' réussie.")
    else:
        print("Erreur : Le signal 'buttonPressed' n'a pas été trouvé dans l'objet QML.")

    # Exécuter l'application
    sys.exit(app.exec())