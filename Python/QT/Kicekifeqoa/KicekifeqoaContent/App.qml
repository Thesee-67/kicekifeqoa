import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 600
    height: 400
    visible: true
    title: "Kicekifeqoa"

    ListModel {
        id: taskModel
    }

    Component.onCompleted: {
        taskHandlerBackend.fetchTasks()
    }

    ListView {
        id: taskListView
        model: taskModel
        anchors.fill: parent

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

                // Bouton pour modifier la tâche
                RoundButton {
                    id: editcard
                    text: "🖌️"
                    Layout.preferredWidth: 80

                    onClicked: {
                        // Chargement dynamique de l'élément PopupUpdateTask à partir de PopupUpdateTask.qml
                        var component = Qt.createComponent("PopupUpdateTask.qml");

                        if (component.status === Component.Ready) {
                            var PopupUpdateTask = component.createObject(parent);

                            if (PopupUpdateTask === null) {
                                console.error("Erreur lors de la création de PopupUpdateTask");
                            } else {
                                if (taskHandlerUpdate) {
                                    // Associer l'ID de la tâche en cours
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
                            console.error("Erreur lors du chargement de PopupUpdateTask.qml");
                        }
                    }
                }

                // Bouton pour supprimer la tâche
                RoundButton {
                    id: deletecard
                    text: "🗑️"
                    Layout.preferredWidth: 80

                    onClicked: {
                        var component = Qt.createComponent("PopupDeleteTask.qml");

                        if (component.status === Component.Ready) {
                            var PopupDeleteTask = component.createObject(parent);

                            if (PopupDeleteTask === null) {
                                console.error("Erreur lors de la création de PopupDeleteTask");
                            } else {
                                if (taskHandlerDelete) {
                                    // Associer l'ID de la tâche en cours
                                    PopupDeleteTask.validateDeleteInfo.connect(taskHandlerDelete.validate_delete_info);
                                } else {
                                    console.error("Erreur : TaskHandler est introuvable.");
                                }
                            }
                        } else {
                            console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                        }
                    }
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
}
