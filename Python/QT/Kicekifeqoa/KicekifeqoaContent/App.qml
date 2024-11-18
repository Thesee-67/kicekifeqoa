import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import QtQuick.Window 2.15


Window {
    visible: true
    color: couleur1
    width: 1000
    height: 800
    title: "Kicekifeqoa"
    flags: Qt.Window | Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowCloseButtonHint
    minimumWidth: 1000
    maximumWidth: 1000
    minimumHeight: 800
    maximumHeight: 800

    property string selectedTaskName: ""
    property string selectedTaskId: ""
    property var selectedDelegate: null

    Rectangle {
        id: rectangle
        x: 26
        y: 22
        width: 955
        height: 754
        color: couleur2
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false

        Image {
            id: image
            x: 12
            y: 11
            width: 100
            height: 96
            source: "logo.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    GridLayout {
        anchors.fill: parent
        anchors.leftMargin: 39
        anchors.rightMargin: 32
        anchors.topMargin: 142
        anchors.bottomMargin: 34
        columns: 4
        columnSpacing: 10

        Rectangle {
            id: taskArea
            color: couleur5
            radius: 10
            border.width: 0
            border.color: couleur6
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
                anchors.topMargin: 51
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root
                    width: 200
                    height: 100
                    radius: 5
                    color: selected ? "#dcdcdc" : "#eeeeee"
                    border.width: 2
                    border.color: couleur2
                    anchors.horizontalCenter: parent.horizontalCenter

                    property bool selected: false

                    MouseArea {
                        id: mouseArea
                        anchors.fill: parent
                        onClicked: {
                            if (root.selected) {
                                root.selected = false
                                selectedDelegate = null
                                selectedTaskId = ""
                                selectedTaskName = ""

                                console.log("Aucune tâche sélectionnée")
                            } else {
                                if (selectedDelegate !== null) {
                                    selectedDelegate.selected = false
                                }

                                root.selected = true
                                selectedDelegate = root

                                selectedTaskId = taskid.text
                                selectedTaskName = taskname.text

                                console.log("Tâche sélectionnée ID:", selectedTaskId)
                                console.log("Tâche sélectionnée Nom:", selectedTaskName)
                            }
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
                        color: couleur7
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
                }
            }

            RoundButton {
                id: addButton
                x: 866
                y: -101
                text: "+"
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

            RoundButton {
                id: modify
                x: 836
                y: -71
                text: "🖌️"
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.margins: 10
                anchors.rightMargin: -651
                anchors.bottomMargin: 655
            }

            RoundButton {
                id: remove
                x: 884
                y: -71
                text: "🗑️"
                anchors.right: parent.right
                anchors.bottom: parent.bottom
                anchors.margins: 10
                anchors.rightMargin: -699
                anchors.bottomMargin: 655
                onClicked: {
                    if (selectedTaskName !== "" && selectedTaskId !== "") {
                        var component = Qt.createComponent("PopupDeleteTask.qml");

                        if (component.status === Component.Ready) {
                            var PopupDeleteTask = component.createObject(parent, {
                                "taskName": selectedTaskName,
                                "taskID": selectedTaskId
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
                    } else {
                        console.error("Erreur : Aucune tâche sélectionnée.");
                    }
                }
            }
        }

        Rectangle {
            id: taskArea2
            color: couleur4
            radius: 10
            border.width: 0
            border.color: couleur6
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
                anchors.topMargin: 51
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root2
                    width: 200
                    height: 100
                    radius: 5
                    color: selected ? "#dcdcdc" : "#eeeeee" // Change la couleur si sélectionnée
                    border.width: 2
                    border.color: couleur2
                    anchors.horizontalCenter: parent.horizontalCenter

                    property bool selected: false

                    MouseArea {
                        id: mouseArea2
                        anchors.fill: parent
                        onClicked: {
                            if (root2.selected) {
                                root2.selected = false
                                selectedDelegate = null
                                selectedTaskId = ""
                                selectedTaskName = ""

                                console.log("Aucune tâche sélectionnée")
                            } else {
                                if (selectedDelegate !== null) {
                                    selectedDelegate.selected = false
                                }

                                root2.selected = true
                                selectedDelegate = root2

                                selectedTaskId = taskid2.text
                                selectedTaskName = taskname2.text

                                console.log("Tâche sélectionnée ID:", selectedTaskId)
                                console.log("Tâche sélectionnée Nom:", selectedTaskName)
                            }
                        }
                    }

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
                        color: couleur7
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
            color: couleur3
            radius: 10
            border.width: 0
            border.color: couleur6
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
                anchors.topMargin: 51
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root3
                    width: 200
                    height: 100
                    radius: 5
                    color: selected ? "#dcdcdc" : "#eeeeee" // Change la couleur si sélectionnée
                    border.width: 2
                    border.color: couleur2
                    anchors.horizontalCenter: parent.horizontalCenter

                    property bool selected: false

                    MouseArea {
                        id: mouseArea3
                        anchors.fill: parent
                        onClicked: {
                            if (root3.selected) {
                                root3.selected = false
                                selectedDelegate = null
                                selectedTaskId = ""
                                selectedTaskName = ""

                                console.log("Aucune tâche sélectionnée")
                            } else {
                                if (selectedDelegate !== null) {
                                    selectedDelegate.selected = false
                                }

                                root3.selected = true
                                selectedDelegate = root3

                                selectedTaskId = taskid3.text
                                selectedTaskName = taskname3.text

                                console.log("Tâche sélectionnée ID:", selectedTaskId)
                                console.log("Tâche sélectionnée Nom:", selectedTaskName)
                            }
                        }
                    }

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
                        color: couleur7
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
            border.width: 2
            border.color: "#afafaf"
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
                anchors.topMargin: 51
                anchors.bottomMargin: 12.5
                spacing: 2

                delegate: Rectangle {
                    id: root4
                    width: 200
                    height: 100
                    radius: 5
                    color: selected ? "#dcdcdc" : "#eeeeee" // Change la couleur si sélectionnée
                    border.width: 2
                    border.color: couleur2
                    anchors.horizontalCenter: parent.horizontalCenter

                    property bool selected: false

                    MouseArea {
                        id: mouseArea4
                        anchors.fill: parent
                        onClicked: {
                            if (root4.selected) {
                                root4.selected = false
                                selectedDelegate = null
                                selectedTaskId = ""
                                selectedTaskName = ""

                                console.log("Aucune tâche sélectionnée")
                            } else {
                                if (selectedDelegate !== null) {
                                    selectedDelegate.selected = false
                                }

                                root4.selected = true
                                selectedDelegate = root4

                                selectedTaskId = taskid4.text
                                selectedTaskName = taskname4.text

                                console.log("Tâche sélectionnée ID:", selectedTaskId)
                                console.log("Tâche sélectionnée Nom:", selectedTaskName)
                            }
                        }
                    }

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
                        color: couleur7
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

    Rectangle {
        id: rectangle1
        x: 146
        y: 33
        width: 719
        height: 96
        color: "#eeeeee"
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false
    }

    Rectangle {
        id: rectangle4
        x: 515
        y: 147
        width: 213
        height: 42
        color: couleur2
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false
    }

    Rectangle {
        id: rectangle3
        x: 280
        y: 147
        width: 213
        height: 42
        color: couleur2
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false
    }

    Rectangle {
        id: rectangle5
        x: 750
        y: 147
        width: 213
        height: 42
        color: couleur2
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false
    }

    Rectangle {
        id: rectangle2
        x: 45
        y: 147
        width: 213
        height: 42
        color: couleur2
        radius: 10
        border.color: couleur6
        border.width: 0
        layer.enabled: false

        Text {
            id: _text
            x: 0
            y: 2
            width: 213
            height: 38
            color: couleur5
            text: qsTr("Urgent")
            font.pixelSize: 28
            horizontalAlignment: Text.AlignHCenter
            font.family: "Verdana"
        }

        Text {
            id: _text1
            x: 234
            y: 2
            width: 213
            height: 38
            color: couleur4
            text: qsTr("En cours")
            font.pixelSize: 28
            horizontalAlignment: Text.AlignHCenter
            font.family: "Verdana"
        }

        Text {
            id: _text2
            x: 470
            y: 2
            width: 213
            height: 38
            color: couleur3
            text: qsTr("A Faire")
            font.pixelSize: 28
            horizontalAlignment: Text.AlignHCenter
            font.family: "Verdana"
        }

        Text {
            id: _text3
            x: 705
            y: 2
            width: 213
            height: 38
            color: "#afafafaf"
            text: qsTr("Fini")
            font.pixelSize: 28
            horizontalAlignment: Text.AlignHCenter
            styleColor: "#afafafaf"
            style: Text.Outline
            font.family: "Verdana"
        }
    }
}
