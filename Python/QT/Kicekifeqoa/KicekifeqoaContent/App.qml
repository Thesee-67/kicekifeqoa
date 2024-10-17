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

    Row {
        anchors.fill: parent

        ListView {
            id: taskListView
            model: taskModel
            width: parent.width * 0.7
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            delegate: Rectangle {
                id: root
                width: 200
                height: 100
                color: "#bcbcbc"
                border.color: "red"
                border.width: 2

                // Activation du glisser
                Drag.active: dragArea.drag.active
                Drag.hotSpot.x: dragArea.width / 2
                Drag.hotSpot.y: dragArea.height / 2
                Drag.source: dragArea

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
                    x: 152
                    y: 2
                    width: 60
                    height: 30
                    text: "Fini ?"
                    hoverEnabled: true
                    icon.color: "#000000"
                    display: AbstractButton.TextBesideIcon
                    autoExclusive: false
                    checked: model.checked === 1
                    scale: 1
                }

                Text {
                    id: priority
                    x: 65
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

                MouseArea {
                    id: dragArea
                    anchors.fill: parent
                    drag.target: root

                    onReleased: {
                        console.log("Item dropped!")
                    }
                }
            }
        }

        Column {
            id: columndropArea
            width: parent.width * 0.3
            height: parent.height
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            DropArea {
                id: dropArea
                anchors.fill: parent
                onDropped: {
                    console.log("Item dropped in the column!")
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
