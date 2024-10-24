import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Window {
    id: loginWindow  // Définition de l'identifiant

    visible: true
    color: "#4e598c"
    width: 600
    height: 580
    title: qsTr("Login")

    // Connexion du signal de succès de login pour fermer la fenêtre
    Connections {
        target: taskHandlerLogin
        function onLoginSuccess() {
            loginWindow.close();  // Fermer la fenêtre login
        }

        function onLoginPasswdFail() {
            _text3.text = "Mot de passe incorrect";  // Affiche un message d'erreur pour le mot de passe
        }

        function onLoginEmailFail() {
            _text3.text = "Email incorrect";  // Affiche un message d'erreur pour l'email
        }
    }

    Rectangle {
        id: rectangle
        x: 20
        y: 20
        width: 560
        height: 546
        color: "#ffffff"
        radius: 10
        border.width: 0
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter

        Rectangle {
            id: rectangle4
            x: 153
            y: 405
            width: 361
            height: 125
            color: "#f9c784"
            radius: 10
            border.width: 0
            anchors.horizontalCenter: parent.horizontalCenter

            Rectangle {
                id: rectangle5
                x: 70
                y: 70
                width: 100
                height: 40
                color: "#ffffff"
                radius: 10
            }

            Rectangle {
                id: rectangle6
                x: 195
                y: 69
                width: 100
                height: 40
                color: "#ffffff"
                radius: 10
                anchors.bottom: rectangle5.bottom
            }
        }

        Rectangle {
            id: rectangle3
            x: 153
            y: 138
            width: 361
            height: 245
            color: "#ff8c42"
            radius: 10
            anchors.bottom: rectangle2.bottom
            anchors.bottomMargin: -139
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: _text1
            x: 229
            y: 155
            width: 103
            height: 42
            color: "#ffffff"
            text: qsTr("E-mail :")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
            font.bold: true
            font.family: "Verdana"
        }

        Rectangle {
            id: rectangle2
            x: 123
            y: 208
            width: 317
            height: 36
            opacity: 1
            color: "#ffffff"
            radius: 10
            clip: false
        }

        TextInput {
            id: textInput1
            x: 128
            y: 208
            width: 304
            height: 36
            text: qsTr("")
            anchors.top: rectangle2.top
            anchors.bottom: rectangle2.bottom
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenter: parent.horizontalCenter
            selectedTextColor: "#ffffff"
            selectionColor: "#f94b7cd9"
        }

        Text {
            id: _text2
            x: 208
            y: 264
            width: 144
            height: 43
            color: "#ffffff"
            text: qsTr("Password :")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
            font.bold: true
            font.family: "Verdana"

            Rectangle {
                id: rectangle1
                x: -84
                y: 47
                width: 315
                height: 36
                opacity: 1
                color: "#ffffff"
                radius: 10
                clip: false
            }
        }

        TextInput {
            id: textInput2
            x: 202
            y: 313
            width: 300
            height: 36
            opacity: 1
            text: qsTr("")
            anchors.top: _text2.bottom
            anchors.topMargin: 6
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.horizontalCenterOffset: 0
            anchors.horizontalCenter: rectangle2.horizontalCenter
            selectionColor: "#f94b7cd9"
            selectedTextColor: "#ffffff"
        }

        Button {
            id: loginButton
            x: 168
            y: 474
            width: 100
            height: 40
            visible: true
            text: qsTr("Login")
            highlighted: false
            flat: true
            icon.color: "#b6d4f2"
            onClicked: {
                taskHandlerLogin.checkCredentials(textInput1.text, textInput2.text)
            }
        }

        Button {
            id: registerButton
            x: 295
            y: 474
            width: 100
            height: 40
            text: qsTr("Register")
            flat: true
            onClicked: {
                // Chargement dynamique de l'élément PopupCreateTask à partir de Register.qml
                var component = Qt.createComponent("Register.qml");

                // Vérification que le fichier QML a été chargé correctement
                if (component.status === Component.Ready) {
                    // Création d'une instance de l'élément Register
                    var Register = component.createObject(parent);
                }
            }
        }


        Image {
            id: image
            x: 230
            y: 18
            width: 102
            height: 101
            source: "logo.png"
        }

        Text {
        id: _text3
        x: 112
        y: 417
        width: 338
        height: 30
        color: "#ffffff"
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
        font.styleName: "Gras"
        font.family: "Verdana"
        anchors.horizontalCenter: rectangle2.horizontalCenter
        }


        states: [
            State {
                name: "clicked"
            }
        ]
    }

}
