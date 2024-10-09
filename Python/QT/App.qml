import QtQuick
import QtQuick.Controls

Rectangle {
    id: rectangle
    width: 640  // Remplacez avec la largeur souhaitée
    height: 480  // Remplacez avec la hauteur souhaitée

    color: "#FFFFFF"  // Remplacez avec la couleur de fond souhaitée

    Button {
        id: button
        text: "Press me"
        anchors.verticalCenter: parent.verticalCenter
        checkable: true
        anchors.horizontalCenter: parent.horizontalCenter

        Connections {
            target: button
            onClicked: animation.start()
        }
    }

    Text {
        id: label
        text: "Hello UntitledProject"
        anchors.top: button.bottom
        font.family: "Arial"  // Remplacez par la police souhaitée
        anchors.topMargin: 45
        anchors.horizontalCenter: parent.horizontalCenter

        SequentialAnimation {
            id: animation

            ColorAnimation {
                id: colorAnimation1
                target: rectangle
                property: "color"
                to: "#2294c6"
                from: "#FFFFFF"
            }

            ColorAnimation {
                id: colorAnimation2
                target: rectangle
                property: "color"
                to: "#FFFFFF"
                from: "#2294c6"
            }
        }
    }

    states: [
        State {
            name: "clicked"
            when: button.checked

            PropertyChanges {
                target: label
                text: "Button Checked"
            }
        }
    ]
}
