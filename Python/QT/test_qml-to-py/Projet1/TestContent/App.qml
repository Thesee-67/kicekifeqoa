import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    width: 600
    height: 400
    visible: true
    title: "To-Do List"

    // ListView pour afficher les tâches
    ListView {
        id: taskListView
        anchors.fill: parent
        model: taskModel.tasks // Utilisation du modèle de tâches
        delegate: Item {
            width: taskListView.width
            height: 50
            Row {
                spacing: 10
                Text {
                    text: modelData.taskName // Nom de la tâche
                    font.pixelSize: 20
                }
                Text {
                    text: "Priorité: " + modelData.taskPriority // Priorité de la tâche
                    font.pixelSize: 16
                }
            }
        }
    }

    RoundButton {
        id: addcard
        x: 43
        y: 351
        text: "+"
        onClicked: {
            var component = Qt.createComponent("Popup.qml");
            if (component.status === Component.Ready) {
                var popup = component.createObject(parent); // Créer une nouvelle instance
                if (popup === null) {
                    console.error("Erreur lors de la création de Popup");
                } else {
                    // Connexion des signaux après la création du popup
                    popup.updateTaskName.connect(taskHandler.update_task_name);
                    popup.updateTaskPriority.connect(taskHandler.update_task_priority);
                    popup.addTag.connect(taskHandler.add_tag);
                    popup.removeLastTag.connect(taskHandler.remove_last_tag);
                    popup.addUser.connect(taskHandler.add_user);
                    popup.removeLastUser.connect(taskHandler.remove_last_user);
                    popup.validateinfo.connect(taskHandler.validate_info);
                }
            } else {
                console.error("Erreur lors du chargement de Popup.qml");
            }
        }
    }

    RoundButton {
        id: roundButton
        x: 180
        y: 241
        text: "🖌"
    }
}
