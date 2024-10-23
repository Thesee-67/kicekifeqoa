import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: register
    visible: true
    width: 400
    height: 400
    title: qsTr("Register")

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 400
        height: 400
        color: "#4E598C"

        Text {
            id: _text
            x: 147
            y: 174
            width: 107
            height: 29
            text: qsTr("Password :")
            font.pixelSize: 25
            horizontalAlignment: Text.AlignHCenter
        }

        Text {
            id: _text1
            x: 153
            y: 69
            width: 95
            height: 33
            text: qsTr("E-mail :")
            font.pixelSize: 25
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            id: button
            x: 150
            y: 307
            width: 100
            height: 40
            text: qsTr("Register")
            onClicked: {
            register.close();  // Fermer la fenêtre login
        }
        }

        Text {
            id: _text2
            x: 104
            y: 8
            width: 193
            height: 40
            text: qsTr("Register")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
        }

        Rectangle {
            id: rectangle1
            x: 87
            y: 118
            width: 226
            height: 36
            color: "#FFFFFF"
        }

        Rectangle {
            id: rectangle2
            x: 87
            y: 235
            width: 226
            height: 36
            color: "#FFFFFF"
        }

        Text {
            id: _text3
            x: 58
            y: 365
            width: 285
            height: 27
            text: qsTr("ttt")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
        }
    }

    TextInput {
        id: textInput2
        x: 87
        y: 118
        width: 225
        height: 36
        text: qsTr("")
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
    }

    TextInput {
        id: textInput3
        x: 87
        y: 235
        width: 225
        height: 35
        text: qsTr("")
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
    }
}
