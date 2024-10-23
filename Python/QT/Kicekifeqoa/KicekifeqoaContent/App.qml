import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    visible: true
    width: 940
    height: 600
    title: "Colonne"

    GridLayout {
        anchors.fill: parent
        columns: 4
        columnSpacing: 10

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
                    radius: 5
                    color: selected ? "#9d9d9d" : "#bcbcbc" // Change la couleur si sélectionnée
                    border.width: 1
                    border.color: "gray"
                    anchors.horizontalCenter: parent.horizontalCenter

                    property bool selected: false // Ajoute une propriété pour gérer la sélection

                    MouseArea {
                        id: mouseArea
                        anchors.fill: parent
                        onClicked: {
                            root.selected = !root.selected // Change l'état de sélection
                            console.log(taskid.text) // Affiche l'ID de la tâche dans le terminal
                        }
                    }

                    Text {
                        id: taskname
                        x: 4
                        y: 6
                        text: qsTr(model.name)
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }
                    Text {
                        id: taskid
                        x: 150
                        y: 25
                        color: "#bcbcbc"
                        text: model.id_task
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
                                var PopupDeleteTask = component.createObject(parent, {
                                    "taskName": taskname.text,
                                    "taskID": taskid.text
                                });

                                if (PopupDeleteTask === null) {
                                    console.error("Erreur lors de la création de PopupDeleteTask");
                                } else {
                                    if (taskHandlerDelete) {
                                        PopupDeleteTask.taskId.connect(taskHandlerDelete.set_task_id);
                                        PopupDeleteTask.validateDeleteInfo.connect(function() {
                                            taskHandlerDelete.validate_delete_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                                    } else {
                                        console.error("Erreur : taskHandlerDelete n'est pas initialisé");
                                    }
                                }
                            } else {
                                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                            }
                        }
                    }
                }
            }

            RoundButton {
                id: addButton
                text: "+"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
                onClicked: {
                    var component = Qt.createComponent("PopupCreateTask.qml");

                    if (component.status === Component.Ready) {
                        var PopupCreateTask = component.createObject(parent);

                        if (PopupCreateTask === null) {
                            console.error("Erreur lors de la création de PopupCreateTask");
                        } else {
                            if (taskHandlerCreate) {
                                PopupCreateTask.addTaskName.connect(taskHandlerCreate.add_task_name);
                                PopupCreateTask.addTaskPriority.connect(taskHandlerCreate.add_task_priority);
                                PopupCreateTask.addTag.connect(taskHandlerCreate.add_tag);
                                PopupCreateTask.removeLastTag.connect(taskHandlerCreate.remove_last_tag);
                                PopupCreateTask.addUser.connect(taskHandlerCreate.add_user);
                                PopupCreateTask.removeLastUser.connect(taskHandlerCreate.remove_last_user);
                                PopupCreateTask.addStartDate.connect(taskHandlerCreate.add_start_date);
                                PopupCreateTask.addEndDate.connect(taskHandlerCreate.add_end_date);
                                PopupCreateTask.taskCompleted.connect(taskHandlerCreate.task_completed);
                                PopupCreateTask.validateInfo.connect(function() {
                                    taskHandlerCreate.validate_info();
                                    taskHandlerBackend.fetchTasks();
                                });
                            } else {
                                console.error("Erreur : TaskHandler est introuvable.");
                            }
                        }
                    } else {
                        console.error("Erreur lors du chargement de PopupCreateTask.qml");
                    }
                }
            }

            Connections {
                target: taskHandlerBackend
                onTasksFetchedPriority2: function (tasks) {
                    taskModel.clear();  // Remplacer par taskModelPriority2
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


        Rectangle {
            id: taskArea2
            color: "#eeeeee"
            radius: 10
            border.width: 1
            border.color: "gray"
            width: 225
            Layout.fillHeight: true

            ListModel {
                id: taskModel2
            }

            Component.onCompleted: {
                taskHandlerBackend.fetchTasks()
            }

            ListView {
                id: taskListView2
                model: taskModel2
                anchors.fill: parent
                anchors.topMargin: 12.5
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root2
                    width: 200
                    height: 100
                    color: "#bcbcbc"
                    radius: 5
                    border.width: 1
                    border.color: "gray"
                    anchors.horizontalCenter: parent.horizontalCenter

                    Text {
                        id: taskname2
                        x: 4
                        y: 6
                        text: qsTr(model.name)
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }
                    Text {
                        id: taskid2
                        x: 150
                        y: 25
                        color: "#bcbcbc"
                        text: model.id_task
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }

                    Text {
                        id: enddate2
                        x: 4
                        y: 57
                        text: model.end_date
                        font.pixelSize: 12
                    }

                    CheckBox {
                        id: checked2
                        x: 152
                        y: 2
                        width: 60
                        height: 30
                        text: "Fini ?"
                        checked: model.checked === 1
                    }

                    Text {
                        id: priority2
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
                        id: tag2
                        x: 4
                        y: 35
                        text: qsTr(model.tag)
                        font.pixelSize: 12
                    }

                    // Bouton de modification
                    RoundButton {
                        id: editcard2
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
                        id: deletecard2
                        x: 165
                        y: 57
                        width: 30
                        height: 30
                        text: "🗑️"
                        onClicked: {
                            var component = Qt.createComponent("PopupDeleteTask.qml");

                            if (component.status === Component.Ready) {
                                var PopupDeleteTask = component.createObject(parent, {
                                    "taskName": taskname2.text,
                                    "taskID": taskid2.text
                                });

                                if (PopupDeleteTask === null) {
                                    console.error("Erreur lors de la création de PopupDeleteTask");
                                } else {
                                    if (taskHandlerDelete) {
                                        PopupDeleteTask.taskId.connect(taskHandlerDelete.set_task_id);
                                        PopupDeleteTask.validateDeleteInfo.connect(function() {
                                            taskHandlerDelete.validate_delete_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                                    } else {
                                        console.error("Erreur : taskHandlerDelete n'est pas initialisé");
                                    }
                                }
                            } else {
                                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                            }
                        }
                    }
                }
            }

            RoundButton {
                id: addButton2
                text: "+"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
                onClicked: {
                    var component = Qt.createComponent("PopupCreateTask.qml");

                    if (component.status === Component.Ready) {
                        var PopupCreateTask = component.createObject(parent);

                        if (PopupCreateTask === null) {
                            console.error("Erreur lors de la création de PopupCreateTask");
                        } else {
                            if (taskHandlerCreate) {
                                PopupCreateTask.addTaskName.connect(taskHandlerCreate.add_task_name);
                                PopupCreateTask.addTaskPriority.connect(taskHandlerCreate.add_task_priority);
                                PopupCreateTask.addTag.connect(taskHandlerCreate.add_tag);
                                PopupCreateTask.removeLastTag.connect(taskHandlerCreate.remove_last_tag);
                                PopupCreateTask.addUser.connect(taskHandlerCreate.add_user);
                                PopupCreateTask.removeLastUser.connect(taskHandlerCreate.remove_last_user);
                                PopupCreateTask.addStartDate.connect(taskHandlerCreate.add_start_date);
                                PopupCreateTask.addEndDate.connect(taskHandlerCreate.add_end_date);
                                PopupCreateTask.taskCompleted.connect(taskHandlerCreate.task_completed);
                                PopupCreateTask.validateInfo.connect(function() {
                                            taskHandlerCreate.validate_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                            } else {
                                console.error("Erreur : TaskHandler est introuvable.");
                            }
                        }
                    } else {
                        console.error("Erreur lors du chargement de PopupCreateTask.qml");
                    }
                }
            }

            Connections {
                target: taskHandlerBackend
                onTasksFetchedPriority1: function (tasks) {
                    taskModel2.clear();  // Remplacer par taskModelPriority1
                    for (var i = 0; i < tasks.length; i++) {
                        taskModel2.append({  // Remplacer taskModel2 par taskModelPriority1
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
        Rectangle {
            id: taskArea3
            color: "#eeeeee"
            radius: 10
            border.width: 1
            border.color: "gray"
            width: 225
            Layout.fillHeight: true

            ListModel {
                id: taskModel3
            }

            Component.onCompleted: {
                taskHandlerBackend.fetchTasks()
            }

            ListView {
                id: taskListView3
                model: taskModel3
                anchors.fill: parent
                anchors.topMargin: 12.5
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root3
                    width: 200
                    height: 100
                    color: "#bcbcbc"
                    radius: 5
                    border.width: 1
                    border.color: "gray"
                    anchors.horizontalCenter: parent.horizontalCenter

                    Text {
                        id: taskname3
                        x: 4
                        y: 6
                        text: qsTr(model.name)
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }
                    Text {
                        id: taskid3
                        x: 150
                        y: 25
                        color: "#bcbcbc"
                        text: model.id_task
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }

                    Text {
                        id: enddate3
                        x: 4
                        y: 57
                        text: model.end_date
                        font.pixelSize: 12
                    }

                    CheckBox {
                        id: checked3
                        x: 152
                        y: 2
                        width: 60
                        height: 30
                        text: "Fini ?"
                        checked: model.checked === 1
                    }

                    Text {
                        id: priority3
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
                        id: tag3
                        x: 4
                        y: 35
                        text: qsTr(model.tag)
                        font.pixelSize: 12
                    }

                    // Bouton de modification
                    RoundButton {
                        id: editcard3
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
                        id: deletecard3
                        x: 165
                        y: 57
                        width: 30
                        height: 30
                        text: "🗑️"
                        onClicked: {
                            var component = Qt.createComponent("PopupDeleteTask.qml");

                            if (component.status === Component.Ready) {
                                var PopupDeleteTask = component.createObject(parent, {
                                    "taskName": taskname3.text,
                                    "taskID": taskid3.text
                                });

                                if (PopupDeleteTask === null) {
                                    console.error("Erreur lors de la création de PopupDeleteTask");
                                } else {
                                    if (taskHandlerDelete) {
                                        PopupDeleteTask.taskId.connect(taskHandlerDelete.set_task_id);
                                        PopupDeleteTask.validateDeleteInfo.connect(function() {
                                            taskHandlerDelete.validate_delete_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                                    } else {
                                        console.error("Erreur : taskHandlerDelete n'est pas initialisé");
                                    }
                                }
                            } else {
                                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                            }
                        }
                    }
                }
            }

            RoundButton {
                id: addButton3
                text: "+"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
                onClicked: {
                    var component = Qt.createComponent("PopupCreateTask.qml");

                    if (component.status === Component.Ready) {
                        var PopupCreateTask = component.createObject(parent);

                        if (PopupCreateTask === null) {
                            console.error("Erreur lors de la création de PopupCreateTask");
                        } else {
                            if (taskHandlerCreate) {
                                PopupCreateTask.addTaskName.connect(taskHandlerCreate.add_task_name);
                                PopupCreateTask.addTaskPriority.connect(taskHandlerCreate.add_task_priority);
                                PopupCreateTask.addTag.connect(taskHandlerCreate.add_tag);
                                PopupCreateTask.removeLastTag.connect(taskHandlerCreate.remove_last_tag);
                                PopupCreateTask.addUser.connect(taskHandlerCreate.add_user);
                                PopupCreateTask.removeLastUser.connect(taskHandlerCreate.remove_last_user);
                                PopupCreateTask.addStartDate.connect(taskHandlerCreate.add_start_date);
                                PopupCreateTask.addEndDate.connect(taskHandlerCreate.add_end_date);
                                PopupCreateTask.taskCompleted.connect(taskHandlerCreate.task_completed);
                                PopupCreateTask.validateInfo.connect(function() {
                                            taskHandlerCreate.validate_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                            } else {
                                console.error("Erreur : TaskHandler est introuvable.");
                            }
                        }
                    } else {
                        console.error("Erreur lors du chargement de PopupCreateTask.qml");
                    }
                }
            }

            Connections {
                target: taskHandlerBackend
                onTasksFetchedPriority0: function (tasks) {
                    taskModel3.clear();  // Remplacer par taskModelPriority0
                    for (var i = 0; i < tasks.length; i++) {
                        taskModel3.append({  // Remplacer taskModel3 par taskModelPriority0
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
        Rectangle {
            id: taskArea4
            color: "#eeeeee"
            radius: 10
            border.width: 1
            border.color: "gray"
            width: 225
            Layout.fillHeight: true

            ListModel {
                id: taskModel4
            }

            Component.onCompleted: {
                taskHandlerBackend.fetchTasks()
            }

            ListView {
                id: taskListView4
                model: taskModel4
                anchors.fill: parent
                anchors.topMargin: 12.5
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root4
                    width: 200
                    height: 100
                    color: "#bcbcbc"
                    radius: 5
                    border.width: 1
                    border.color: "gray"
                    anchors.horizontalCenter: parent.horizontalCenter

                    Text {
                        id: taskname4
                        x: 4
                        y: 6
                        text: qsTr(model.name)
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }
                    Text {
                        id: taskid4
                        x: 150
                        y: 25
                        color: "#bcbcbc"
                        text: model.id_task
                        font.pixelSize: 17
                        font.styleName: "Gras"
                    }

                    Text {
                        id: enddate4
                        x: 4
                        y: 57
                        text: model.end_date
                        font.pixelSize: 12
                    }

                    CheckBox {
                        id: checked4
                        x: 152
                        y: 2
                        width: 60
                        height: 30
                        text: "Fini ?"
                        checked: model.checked === 1
                    }

                    Text {
                        id: priority4
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
                        id: tag4
                        x: 4
                        y: 35
                        text: qsTr(model.tag)
                        font.pixelSize: 12
                    }

                    // Bouton de modification
                    RoundButton {
                        id: editcard4
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
                        id: deletecard4
                        x: 165
                        y: 57
                        width: 30
                        height: 30
                        text: "🗑️"
                        onClicked: {
                            var component = Qt.createComponent("PopupDeleteTask.qml");

                            if (component.status === Component.Ready) {
                                var PopupDeleteTask = component.createObject(parent, {
                                    "taskName": taskname4.text,
                                    "taskID": taskid4.text
                                });

                                if (PopupDeleteTask === null) {
                                    console.error("Erreur lors de la création de PopupDeleteTask");
                                } else {
                                    if (taskHandlerDelete) {
                                        PopupDeleteTask.taskId.connect(taskHandlerDelete.set_task_id);
                                        PopupDeleteTask.validateDeleteInfo.connect(function() {
                                            taskHandlerDelete.validate_delete_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                                    } else {
                                        console.error("Erreur : taskHandlerDelete n'est pas initialisé");
                                    }
                                }
                            } else {
                                console.error("Erreur lors du chargement de PopupDeleteTask.qml");
                            }
                        }
                    }
                }
            }

            RoundButton {
                id: addButton4
                text: "+"
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                anchors.margins: 10
                onClicked: {
                    var component = Qt.createComponent("PopupCreateTask.qml");

                    if (component.status === Component.Ready) {
                        var PopupCreateTask = component.createObject(parent);

                        if (PopupCreateTask === null) {
                            console.error("Erreur lors de la création de PopupCreateTask");
                        } else {
                            if (taskHandlerCreate) {
                                PopupCreateTask.addTaskName.connect(taskHandlerCreate.add_task_name);
                                PopupCreateTask.addTaskPriority.connect(taskHandlerCreate.add_task_priority);
                                PopupCreateTask.addTag.connect(taskHandlerCreate.add_tag);
                                PopupCreateTask.removeLastTag.connect(taskHandlerCreate.remove_last_tag);
                                PopupCreateTask.addUser.connect(taskHandlerCreate.add_user);
                                PopupCreateTask.removeLastUser.connect(taskHandlerCreate.remove_last_user);
                                PopupCreateTask.addStartDate.connect(taskHandlerCreate.add_start_date);
                                PopupCreateTask.addEndDate.connect(taskHandlerCreate.add_end_date);
                                PopupCreateTask.taskCompleted.connect(taskHandlerCreate.task_completed);
                                PopupCreateTask.validateInfo.connect(function() {
                                            taskHandlerCreate.validate_info();
                                            taskHandlerBackend.fetchTasks();
                                        });
                            } else {
                                console.error("Erreur : TaskHandler est introuvable.");
                            }
                        }
                    } else {
                        console.error("Erreur lors du chargement de PopupCreateTask.qml");
                    }
                }
            }

            Connections {
                target: taskHandlerBackend
                 onTasksFetchedChecked: function (tasks) {
                    taskModel4.clear();
                    for (var i = 0; i < tasks.length; i++) {
                        taskModel4.append({
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
