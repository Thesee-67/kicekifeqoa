import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 600
    height: 400
    visible: true
    title: "Kicekifeqoa"

    // Modèle pour gérer les données de la base de données Task
    ListModel {
        id: taskModel
    }

    // Charger les tâches lors du démarrage de l'application
    Component.onCompleted: {
        taskHandlerBackend.fetchTasks()
    }

    // Liste des tâches à afficher
    ListView {
        id: taskListView
        model: taskModel
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: addcard.top  // La liste occupe tout l'espace au-dessus des boutons

        delegate: Item {
            width: parent.width
            height: 50

            RowLayout {
                Text {
                    text: model.name
                    Layout.preferredWidth: 150
                }
                Text {
                    text: "Priority: " + model.priority
                    Layout.preferredWidth: 100
                }
                Text {
                    text: "End: " + model.end_date
                    Layout.preferredWidth: 150
                }
                Text {
                    text: "Checked: " + model.checked
                    Layout.preferredWidth: 100
                }
                Text {
                    text: "Tag: " + model.tag
                    Layout.preferredWidth: 150
                }
            }
        }
    }

    Connections {
        target: taskHandlerBackend
        onTasksFetched: function(tasks) {
            taskModel.clear()
            for (var i = 0; i < tasks.length; i++) {
                taskModel.append({
                    "id_task": tasks[i].id_task,
                    "name": tasks[i].name,
                    "end_date": tasks[i].end_date,
                    "checked": tasks[i].checked,
                    "priority": tasks[i].priority,
                    "tag": tasks[i].tag
                })
            }
        }
    }

    // Bouton rond pour ajouter une nouvelle tâche
    RoundButton {
        id: addcard
        x: 240
        y: 350
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

                    if (taskHandlerCreate) {  // S'assurer que taskHandler est disponible
                        PopupCreateTask.addTaskName.connect(taskHandlerCreate.add_task_name);
                        PopupCreateTask.addTaskPriority.connect(taskHandlerCreate.add_task_priority);
                        PopupCreateTask.addTag.connect(taskHandlerCreate.add_tag);
                        PopupCreateTask.removeLastTag.connect(taskHandlerCreate.remove_last_tag);
                        PopupCreateTask.addUser.connect(taskHandlerCreate.add_user);
                        PopupCreateTask.removeLastUser.connect(taskHandlerCreate.remove_last_user);
                        PopupCreateTask.addStartDate.connect(taskHandlerCreate.add_start_date);
                        PopupCreateTask.addEndDate.connect(taskHandlerCreate.add_end_date);
                        PopupCreateTask.taskCompleted.connect(taskHandlerCreate.task_completed);
                        PopupCreateTask.validateInfo.connect(taskHandlerCreate.validate_info);
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

    // Bouton rond pour modifier une tâche
    RoundButton {
        id: editcard
        x: 280
        y: 350
        text: "🖌️"

        // Action au clic du bouton
        onClicked: {
            // Chargement dynamique de l'élément PopupUpdateTask à partir de PopupUpdateTask.qml
            var component = Qt.createComponent("PopupUpdateTask.qml");

            // Vérification que le fichier QML a été chargé correctement
            if (component.status === Component.Ready) {
                // Création d'une instance de l'élément PopupUpdateTask
                var PopupUpdateTask = component.createObject(parent);

                // Si l'objet PopupUpdateTask n'a pas pu être créé, afficher un message d'erreur
                if (PopupUpdateTask === null) {
                    console.error("Erreur lors de la création de PopupUpdateTask");
                } else {

                    if (taskHandlerUpdate) {  // S'assurer que taskHandler est disponible
                        PopupUpdateTask.updateTaskName.connect(taskHandlerUpdate.update_task_name);
                        PopupUpdateTask.updateTaskPriority.connect(taskHandlerUpdate.update_task_priority);
                        PopupUpdateTask.addTag.connect(taskHandlerUpdate.add_tag);
                        PopupUpdateTask.removeLastTag.connect(taskHandlerUpdate.remove_last_tag);
                        PopupUpdateTask.addUser.connect(taskHandlerUpdate.add_user);
                        PopupUpdateTask.removeLastUser.connect(taskHandlerUpdate.remove_last_user);
                        PopupUpdateTask.updateStartDate.connect(taskHandlerUpdate.update_start_date);
                        PopupUpdateTask.updateEndDate.connect(taskHandlerUpdate.update_end_date);
                        PopupUpdateTask.taskCompleted.connect(taskHandlerUpdate.task_completed);
                        PopupUpdateTask.validateUpdateInfo.connect(taskHandlerUpdate.validate_update_info);
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

    // Bouton rond pour supprimer une tâche
    RoundButton {
        id: deletecard
        x: 321
        y: 350
        text: "🗑️"

        // Action au clic du bouton
        onClicked: {
            // Chargement dynamique de l'élément PopupDeleteTask à partir de PopupDeleteTask.qml
            var component = Qt.createComponent("PopupDeleteTask.qml");

            // Vérification que le fichier QML a été chargé correctement
            if (component.status === Component.Ready) {
                // Création d'une instance de l'élément PopupDeleteTask
                var PopupDeleteTask = component.createObject(parent);

                // Si l'objet PopupDeleteTask n'a pas pu être créé, afficher un message d'erreur
                if (PopupDeleteTask === null) {
                    console.error("Erreur lors de la création de PopupDeleteTask");

                } else {
                    if (taskHandlerDelete) {
                        PopupDeleteTask.validateDeleteInfo.connect(taskHandlerDelete.validate_delete_info);
                    } else {
                        console.error("Erreur : TaskHandler est introuvable.");
                    }
                }
            } else {
                // Gestion d'erreur en cas de problème lors du chargement du fichier QML
                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
            }
        }
    }
}
