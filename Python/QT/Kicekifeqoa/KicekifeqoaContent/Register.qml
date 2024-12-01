import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Window {
    id: registerWindow
    visible: true
    width: 400
    height: 400

    Connections {
        target: taskHandlerRegister
        onRegisterSuccess: {
            registerWindow.close();  // Fermer la fenêtre register
        }
        onAlreadyMail: {
            _text3.text = "Mail déjà existant";  // Affiche un message d'erreur pour le email
        }
        onBadMail: {
            _text3.text = "Ce mail n'existe pas";  // Affiche un message d'erreur pour le email
        }
        onShortPass: {
            _text3.text = "Mot de passe trop court (8 caractères min)";  // Affiche un message d'erreur pour le mdp
        }
         onLongPass: {
            _text3.text = "Mot de passe trop long (72 caractères max)";  // Affiche un message d'erreur pour le mdp
        }
        onUppercasePass: {
            _text3.text = "Le mot de passe doit contenir une majuscule";  // Affiche un message d'erreur pour le mdp
        }
        onLowercasePass: {
            _text3.text = "Le mot de passe doit contenir une minuscule";  // Affiche un message d'erreur pour le mdp
        }
        onNumberPass: {
            _text3.text = "Le mot de passe doit contenir un nombre";  // Affiche un message d'erreur pour le mdp
        }
        onSpecialPass: {
            _text3.text = "Le mot de passe doit contenir (!@#$%^&*(),.?{}|<>) ";  // Affiche un message d'erreur pour le mdp
        }
        onUnknownError: {
            _text3.text = "Une erreur inconnu s'est produite";  // Affiche un message d'erreur pour le mdp
        }
    }
    Rectangle {
        x: 0
        y: 0
        width: 400
        height: 400
        color: Colors.couleur1
        Rectangle {
        id: rectangle
        x: 9
        y: 9
        width: 380
        height: 382
        color: Colors.couleur2
        radius: 5
        border.width: 0


        Rectangle {
            id: rectangle1
            x: 36
            y: 12
            width: 307
            height: 89
            color: Colors.couleur5
            radius: 5
        }

        Rectangle {
            id: rectangle3
            x: 36
            y: 123
            width: 307
            height: 244
            color: Colors.couleur3
            radius: 5
        }

        Rectangle {
            id: rectangle4
            x: 141
            y: 320
            width: 98
            height: 40
            color: Colors.couleur2
            radius: 5
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Text {
            id: _text
            x: 77
            y: 218
            width: 227
            height: 33
            color: Colors.couleur2
            text: qsTr("Password :")
            font.pixelSize: 25
            horizontalAlignment: Text.AlignHCenter
            font.bold: true
            font.family: "Verdana"
        }

        Text {
            id: _text2
            x: 77
            y: 130
            width: 227
            height: 33
            color: Colors.couleur2
            text: qsTr("E-mail :")
            font.pixelSize: 25
            horizontalAlignment: Text.AlignHCenter
            font.bold: true
            font.family: "Verdana"
        }

        Button {
            id: button
            x: 140
            y: 320
            width: 98
            height: 40
            text: qsTr("Register")
            anchors.horizontalCenter: _text2.horizontalCenter
            flat: true
            onClicked: {
                taskHandlerRegister.checkCredentials(textInput2.text, textInput3.text)
            }
        }

        Text {
            id: _text3
            x: 36
            y: 36
            width: 307
            height: 40
            color: Colors.couleur2
            text: qsTr("Créer un compte")
            font.pixelSize: 30
            horizontalAlignment: Text.AlignHCenter
            font.bold: true
            font.family: "Verdana"
        }

        Rectangle {
            id: rectangle5
            x: 47
            y: 163
            width: 256
            height: 36
            color: Colors.couleur2
            radius: 5
            anchors.left: rectangle2.left
            anchors.right: rectangle2.right
            anchors.rightMargin: 0
        }

        Rectangle {
            id: rectangle2
            x: 77
            y: 251
            width: 286
            height: 36
            color: Colors.couleur2
            radius: 5
            anchors.left: _text2.left
            anchors.bottom: _text1.top
            anchors.leftMargin: -30
            anchors.bottomMargin: 6
        }

        Text {
            id: _text4
            x: 48
            y: 293
            width: 285
            height: 27
            text: qsTr("")
            anchors.top: rectangle2.bottom
            anchors.topMargin: 6
            anchors.bottomMargin: 6
            color: "#e91717"
            font.pixelSize: 20
            anchors.horizontalCenter: parent.horizontalCenter
        }



    }

    TextInput {
        id: textInput2
        x: 65
        y: 172
        width: 264
        height: 36
        text: qsTr("")
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter


    TextInput {
        id: textInput3
        x: 0
        y: 89
        width: 264
        height: 35
        text: qsTr("")
        anchors.left: parent.left
        anchors.leftMargin: 0
        font.pixelSize: 20
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
}
}