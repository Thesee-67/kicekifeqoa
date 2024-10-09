import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QUrl

if __name__ == "__main__":
    # Créer une application Qt
    app = QApplication(sys.argv)

    # Créer une vue rapide pour charger l'interface QML
    view = QQuickView()

    # Charger le fichier QML (assurez-vous que le chemin est correct)
    qml_file = QUrl("App.qml")  # Mettez ici le chemin vers votre fichier QML
    view.setSource(qml_file)

    # Afficher la fenêtre
    view.show()

    # Exécuter l'application
    sys.exit(app.exec())
