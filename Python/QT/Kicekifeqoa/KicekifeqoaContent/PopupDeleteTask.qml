import QtQuick
import QtQuick.Controls

Window {
    id: popupdelete
    visible: true
    color: "#00ffffff"
    width: 200
    height: 100
    opacity: 1
    title: "Supprimer Tâche"
    flags: Qt.FramelessWindowHint

    property string taskName: ""
    property string taskID: ""

    signal taskId(int taskID);
    signal validateDeleteInfo();

    Rectangle {
        id: root
        width: 200
        height: 100
        color: "#4e598c"
        radius: 10
        Rectangle {
            id: rectangle
            x: 5
            y: 5
            width: 190
            height: 90
            radius: 10
            border.width: 0
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            Text {
                id: _text
            x: 19
            y: 3
            text: qsTr("Vous allez supprimer la tâche :")
            font.pixelSize: 12
            anchors.horizontalCenter: parent.horizontalCenter
        }

        RoundButton {
            id: validate
            x: 71
            y: 63
            width: 25
            height: 24
            text: "\u2705"
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 8
            onClicked: {
                taskId(taskID);
                validateDeleteInfo();
                popupdelete.close();
            }
        }

        RoundButton {
            id: cancel
            x: 102
            y: 63
            width: 25
            height: 24
            text: "\u274c"
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 8
            onClicked: {
                popupdelete.close();
            }
        }

        Text {
            id: tasknametext
            x: 19
            y: 25
            width: 158
            height: 25
            text: taskName
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
            anchors.horizontalCenter: parent.horizontalCenter
        }
    }
}
}