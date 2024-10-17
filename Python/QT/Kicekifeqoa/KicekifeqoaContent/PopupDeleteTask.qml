import QtQuick
import QtQuick.Controls
import QtQuick.Window

Window {
    id: popupdelete
    visible: true
    width: 200
    height: 100
    title: "Supprimer Tâche"

    signal taskName(string taskname);
    signal validateDeleteInfo();

    Rectangle {
        id: root
        width: 200
        height: 100

        Text {
            id: _text
            x: 21
            y: 8
            text: qsTr("Vous allez supprimer la tâche :")
            font.pixelSize: 12
        }

        RoundButton {
            id: validate
            x: 73
            y: 68
            width: 25
            height: 24
            text: "\u2705"
            onClicked: {
                taskName(tasknametext.text);
                validateDeleteInfo();
                popupdelete.close();
            }
        }

        RoundButton {
            id: cancel
            x: 104
            y: 68
            width: 25
            height: 24
            text: "\u274c"
            onClicked: {
                popupdelete.close();
            }
        }

        Text {
            id: tasknametext
            x: 21
            y: 30
            width: 158
            height: 25
            text: qsTr("TESTTEST")
            font.pixelSize: 18
            horizontalAlignment: Text.AlignHCenter
        }
    }
}
