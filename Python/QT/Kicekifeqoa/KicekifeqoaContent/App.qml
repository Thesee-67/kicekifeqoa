import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    width: 600
    height: 400
    visible: true
    title: "Kicekifeqoa"

    // Bouton rond pour ajouter une nouvelle tâche
    RoundButton {
        id: addcard
        x: 280
        y: 180
        text: "+"

        // Action au clic du bouton
        onClicked: {
            // Chargement dynamique de l'élément PopupCreateTask à partir de PopupCreateTask.qml
            var component = Qt.createComponent("PopupCreateTask.qml");

            // Vérification que le fichier QML a été chargé correctement
            if (component.status === Component.Ready) {
                // Création d'une instance de l'élément PopupCreateTask
                var PopupCreateTask = component.createObject(parent);

                // Si l'objet PopupCreateTask n'a pas pu être créé, afficher un message d'erreur
                if (PopupCreateTask === null) {
                    console.error("Erreur lors de la création de PopupCreateTask");
                } else {
                    // Connexion des signaux du PopupCreateTask aux slots Python de TaskHandler
                    // Ces signaux sont utilisés pour transférer des données de la vue QML vers la logique Python

                    if (taskHandler) {  // S'assurer que taskHandler est disponible
                        PopupCreateTask.addTaskName.connect(taskHandler.add_task_name);
                        PopupCreateTask.addTaskPriority.connect(taskHandler.add_task_priority);
                        PopupCreateTask.addTag.connect(taskHandler.add_tag);
                        PopupCreateTask.removeLastTag.connect(taskHandler.remove_last_tag);
                        PopupCreateTask.addUser.connect(taskHandler.add_user);
                        PopupCreateTask.removeLastUser.connect(taskHandler.remove_last_user);
                        PopupCreateTask.addStartDate.connect(taskHandler.add_start_date);
                        PopupCreateTask.addEndDate.connect(taskHandler.add_end_date);
                        PopupCreateTask.taskCompleted.connect(taskHandler.task_completed);
                        PopupCreateTask.validateInfo.connect(taskHandler.validate_info);
                    } else {
                        console.error("Erreur : TaskHandler est introuvable.");
                    }
                }
            } else {
                // Gestion d'erreur en cas de problème lors du chargement du fichier QML
                console.error("Erreur lors du chargement de PopupCreateTask.qml");
            }
        }
    }

    // Bouton rond pour ajouter une nouvelle tâche
    RoundButton {
        id: editcard
        x: 320
        y: 180
        text: "🖌️"

        // Action au clic du bouton
        onClicked: {
            // Chargement dynamique de l'élément PopupUpdateTask à partir de PopupUpdateTask.qml
            var component2 = Qt.createComponent("PopupUpdateTask.qml");

            // Vérification que le fichier QML a été chargé correctement
            if (component2.status === Component.Ready) {
                // Création d'une instance de l'élément PopupUpdateTask
                var PopupUpdateTask = component2.createObject(parent);

                // Si l'objet PopupUpdateTask n'a pas pu être créé, afficher un message d'erreur
                if (PopupUpdateTask === null) {
                    console.error("Erreur lors de la création de PopupUpdateTask");
                } else {
                    // Connexion des signaux du PopupUpdateTask aux slots Python de TaskHandler
                    // Ces signaux sont utilisés pour transférer des données de la vue QML vers la logique Python

                    if (taskHandler) {  // S'assurer que taskHandler est disponible
                        PopupUpdateTask.UpdateTaskName.connect(taskHandler.update_task_name);
                        PopupUpdateTask.UpdateTaskPriority.connect(taskHandler.update_task_priority);
                        PopupUpdateTask.addTag.connect(taskHandler.add_tag);
                        PopupUpdateTask.removeLastTag.connect(taskHandler.remove_last_tag);
                        PopupUpdateTask.addUser.connect(taskHandler.add_user);
                        PopupUpdateTask.removeLastUser.connect(taskHandler.remove_last_user);
                        PopupUpdateTask.UpdateStartDate.connect(taskHandler.update_start_date);
                        PopupUpdateTask.UpdateEndDate.connect(taskHandler.update_end_date);
                        PopupUpdateTask.validateUpdateInfo.connect(taskHandler.validate_update_info);
                    } else {
                        console.error("Erreur : TaskHandler est introuvable.");
                    }
                }
            } else {
                // Gestion d'erreur en cas de problème lors du chargement du fichier QML
                console.error("Erreur lors du chargement de PopupUpdateTask.qml");
            }
        }
    }
}
