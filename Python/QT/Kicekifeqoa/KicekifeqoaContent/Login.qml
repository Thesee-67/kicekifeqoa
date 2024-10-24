import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: loginWindow  // Définition de l'identifiant

    visible: true
    width: 600
    height: 700
    title: qsTr("Login")

    // Connexion du signal de succès de login pour fermer la fenêtre
    Connections {
        target: taskHandlerLogin
        onLoginSuccess: {
            loginWindow.close();  // Fermer la fenêtre login
        }

        onLoginPasswdFail: {
            _text3.text = "Mot de passe incorrect";  // Affiche un message d'erreur pour le mot de passe
        }

        onLoginEmailFail: {
            _text3.text = "Email incorrect";  // Affiche un message d'erreur pour l'email
        }
    }

    Rectangle {
        id: rectangle
        width: 600
        height: 700
        color: "#4E598C"

        Text {
            id: _text
            x: 196
            y: 48
            width: 208
            height: 63
            text: qsTr("Kicékiféqoa")
            font.pixelSize: 40
            horizontalAlignment: Text.AlignHCenter
            font.underline: false
        }

        Text {
            id: _text1
            x: 249
            y: 157
            width: 103
            height: 42
            text: qsTr("E-mail :")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
        }

        Rectangle {
            id: rectangle2
            x: 188
            y: 226
            width: 226
            height: 36
            opacity: 1
            color: "#F9C784"
            clip: false
        }

        TextInput {
            id: textInput1
            x: 220
            y: 226
            width: 161
            height: 36
            text: qsTr("")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            selectedTextColor: "#ffffff"
            selectionColor: "#f94b7cd9"
        }

        Text {
            id: _text2
            x: 234
            y: 280
            width: 144
            height: 43
            text: qsTr("Password :")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter

            Rectangle {
                id: rectangle1
                x: -46
                y: 71
                width: 226
                height: 36
                opacity: 1
                color: "#F9C784"
                clip: false
            }
        }

        TextInput {
            id: textInput2
            x: 222
            y: 352
            width: 156
            height: 32
            opacity: 1
            text: qsTr("")
            font.pixelSize: 20
            horizontalAlignment: Text.AlignHCenter
            selectionColor: "#f94b7cd9"
            selectedTextColor: "#ffffff"
        }

        Button {
            id: loginButton
            x: 250
            y: 462
            width: 100
            height: 40
            text: qsTr("Login")
            icon.color: "#b6d4f2"
            onClicked: {
                taskHandlerLogin.checkCredentials(textInput1.text, textInput2.text)
            }
        }

        Button {
            id: registerButton
            x: 250
            y: 557
            width: 100
            height: 40
            text: qsTr("Register")
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

        Rectangle {
            id: rectangle3
            x: 28
            y: 30
            width: 102
            height: 101
            color: "#FFFFFF"
        }

        Image {
            id: image
            x: 28
            y: 30
            width: 102
            height: 101
            source: "img.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
        id: _text3
        x: 188
        y: 415
        width: 226
        height: 30
        color: "#e91717"
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
    }

        states: [
            State {
                name: "clicked"
            }
        ]
    }

}