import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    width: 600
    height: 400
    visible: true
    title: "Test"

    // Bouton rond pour ajouter une nouvelle tâche
    RoundButton {
        id: addcard
        x: 280
        y: 180
        text: "+"

        // Action au clic du bouton
        onClicked: {
            // Chargement dynamique de l'élément Popup à partir de Popup.qml
            var component = Qt.createComponent("Popup.qml");

            // Vérification que le fichier QML a été chargé correctement
            if (component.status === Component.Ready) {
                // Création d'une instance de l'élément Popup
                var popup = component.createObject(parent);

                // Si l'objet Popup n'a pas pu être créé, afficher un message d'erreur
                if (popup === null) {
                    console.error("Erreur lors de la création de Popup");
                } else {
                    // Connexion des signaux du Popup aux slots Python de TaskHandler
                    // Ces signaux sont utilisés pour transférer des données de la vue QML vers la logique Python

                    if (taskHandler) {  // S'assurer que taskHandler est disponible
                        popup.addTaskName.connect(taskHandler.add_task_name);
                        popup.addTaskPriority.connect(taskHandler.add_task_priority);
                        popup.addTag.connect(taskHandler.add_tag);
                        popup.removeLastTag.connect(taskHandler.remove_last_tag);
                        popup.addUser.connect(taskHandler.add_user);
                        popup.removeLastUser.connect(taskHandler.remove_last_user);
                        popup.addStartDate.connect(taskHandler.add_start_date);
                        popup.addEndDate.connect(taskHandler.add_end_date);
                        popup.validateInfo.connect(taskHandler.validate_info);
                    } else {
                        console.error("Erreur : TaskHandler est introuvable.");
                    }
                }
            } else {
                // Gestion d'erreur en cas de problème lors du chargement du fichier QML
                console.error("Erreur lors du chargement de Popup.qml");
            }
        }
    }
}
