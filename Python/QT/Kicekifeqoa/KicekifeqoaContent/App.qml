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

        delegate: Rectangle {
            id: root
            width: 200
            height: 100
            color: "#bcbcbc"

            Text {
                id: taskname
                x: 4
                y: 6
                width: 33
                height: 23
                text: qsTr(model.name)
                font.pixelSize: 17
                font.styleName: "Gras"
            }

            Text {
                id: enddate
                x: 4
                y: 57
                text: model.end_date
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
            }

            CheckBox {
                id: checked
                x: 168
                y: 2
                width: 30
                height: 30
                text: model.checked
                hoverEnabled: true
                icon.color: "#000000"
                display: AbstractButton.TextBesideIcon
                autoExclusive: false
                checked: false
                scale: 0.6
            }

            Text {
                id: priority
                x: 56
                y: 57
                font.pixelSize: 12
                text: {
                    if (model.priority === 1) {
                        return "🕐";
                    } else if (model.priority === 2) {
                        return "⚠️";
                    } else {
                        return "";
                    }
                }
            }

            Text {
                id: tag
                x: 4
                y: 35
                text: qsTr(model.tag)
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
            }

            RoundButton {
                id: editcard
                x: 132
                y: 67
                width: 30
                height: 30
                text: "🖌️"
                font.pixelSize: 12

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
                x: 165
                y: 67
                width: 30
                height: 30
                text: "🗑️"
                font.pixelSize: 12

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

    Connections {
        target: taskHandlerBackend
        onTasksFetched: function (tasks) {
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
