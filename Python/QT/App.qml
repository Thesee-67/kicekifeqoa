import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Test Application"

    // Définition du signal dans le composant racine
    signal buttonPressed()

    Rectangle {
        id: rectangle
        width: parent.width
        height: parent.height
        color: "#FFFFFF"

        Button {
            id: button
            text: qsTr("Press me")
            anchors.centerIn: parent
            checkable: true

            // Emission du signal buttonPressed lors du clic
            onClicked: {
                buttonPressed()  // Emission du signal
            }
        }
    }
}