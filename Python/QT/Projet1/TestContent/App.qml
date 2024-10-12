import QtQuick
import QtQuick.Controls 6.7

Window {
    width: 600
    height: 400
    visible: true
    title: "Test"

    RoundButton {
        id: addcard
        x: 280
        y: 180
        text: "+"
        onClicked: {
            var component = Qt.createComponent("Popup.qml");
            if (component.status === Component.Ready) {
                var popup = component.createObject(parent); // Créer une nouvelle instance
                if (popup === null) {
                    console.error("Erreur lors de la création de Popup");
                }
            } else {
                console.error("Erreur lors du chargement de Popup.qml");
            }
        }
    }
}
