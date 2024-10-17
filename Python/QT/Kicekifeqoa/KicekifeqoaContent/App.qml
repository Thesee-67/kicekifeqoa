import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 225
    height: 600
    title: "Colonne"

    GridLayout {
        anchors.fill: parent
        columns: 4
        columnSpacing: 20

        // Première colonne - Liste de tâches
        Rectangle {
            id: taskArea
            color: "#eeeeee"
            radius: 10
            border.width: 1
            border.color: "gray"
            width: 225
            Layout.fillHeight: true

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
                anchors.topMargin: 12.5
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root
                    width: 200
                    height: 100
                    color: "#bcbcbc"
                    radius: 5
                    border.width: 1
                    border.color: "gray"
                    anchors.horizontalCenter: parent.horizontalCenter

                    Text {
                        id: taskname
                        x: 4
                        y: 6
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
                    }

                    CheckBox {
                        id: checked
                        x: 152
                        y: 2
                        width: 60
                        height: 30
                        text: "Fini ?"
                        checked: model.checked === 1
                    }

                    Text {
                        id: priority
                        x: 65
                        y: 56
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
                    }

                    // Bouton de modification
                    RoundButton {
                        id: editcard
                        x: 132
                        y: 57
                        width: 30
                        height: 30
                        text: "🖌️"
                        onClicked: {
                            var component = Qt.createComponent("PopupUpdateTask.qml");

                            if (component.status === Component.Ready) {
                                var PopupUpdateTask = component.createObject(parent);

                                if (PopupUpdateTask === null) {
                                    console.error("Erreur lors de la création de PopupUpdateTask");
                                } else {
                                    if (taskHandlerUpdate) {
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
                        y: 57
                        width: 30
                        height: 30
                        text: "🗑️"
                        onClicked: {
                            var component = Qt.createComponent("PopupDeleteTask.qml");

                            if (component.status === Component.Ready) {
                                var PopupDeleteTask = component.createObject(parent);

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
                                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                            }
                        }
                    }
                }
            }

            Connections {
                target: taskHandlerBackend
                onTasksFetched: function (tasks) {
                    taskModel.clear();
                    for (var i = 0; i < tasks.length; i++) {
                        taskModel.append({
                            "id_task": tasks[i].id_task,
                            "name": tasks[i].name,
                            "end_date": tasks[i].end_date,
                            "checked": tasks[i].checked,
                            "priority": tasks[i].priority,
                            "tag": tasks[i].tag
                        });
                    }
                }
            }
        }
    }
}
