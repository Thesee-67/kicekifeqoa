import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    visible: true
    width: 400
    height: 200
    title: "Nouvelle Tâche"

    signal updateTaskName(string name)
    signal updateTaskPriority(int priority)
    signal addTag(string tag)
    signal removeLastTag()
    signal addUser(string email)
    signal removeLastUser()
    signal printAllInfo()

    property var tagsListModel: []
    property var usersListModel: []

    Slider {
        id: priorityslider
        x: 271
        y: 12
        width: 115
        height: 30
        value: 0
        stepSize: 1
        live: true
        to: 2
        hoverEnabled: true
        enabled: true
        topPadding: 6
    }

    RoundButton {
        id: tagadd
        x: 177
        y: 68
        width: 20
        height: 20
        text: "+"
        onClicked: {
            addTag(tagname.text)
            tagname.text = ""
        }
    }

    RoundButton {
        id: tagremove
        x: 203
        y: 68
        width: 20
        height: 20
        text: "-"
        onClicked: {
            removeLastTag()
        }
    }

    SwipeDelegate {
        id: swipeDelegate
        x: -858
        y: 330
        text: qsTr("Swipe Delegate")
    }

    RoundButton {
        id: validate
        x: 352
        y: 152
        text: "\u2713"
        font.pointSize: 15
        onClicked: {
            updateTaskName(tagname.text)
            updateTaskPriority(priorityslider.value)
            printAllInfo()
        }
    }

    Text {
        id: prioritytext
        x: 271
        y: 40
        width: 115
        height: 16
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        text: priorityslider.value === 0 ? "Priorité basse"
             : priorityslider.value === 1 ? "Priorité moyenne"
             : "URGENT"
    }

    TextField {
        id: tagname
        x: 16
        y: 63
        width: 155
        height: 30
        placeholderText: qsTr("Etiquettes")
    }

    RoundButton {
        id: useradd
        x: 177
        y: 104
        width: 20
        height: 20
        text: "+"
        onClicked: {
            addUser(username.text)
            username.text = ""
        }
    }

    RoundButton {
        id: userremove
        x: 203
        y: 104
        width: 20
        height: 20
        text: "-"
        onClicked: {
            removeLastUser()
        }
    }

    TextField {
        id: username
        x: 16
        y: 99
        width: 155
        height: 30
        placeholderText: qsTr("Utilisateurs / Groupes")
    }

    TextField {
        id: taskname
        x: 16
        y: 12
        width: 181
        height: 30
        placeholderText: qsTr("Nom de la tâche")
    }

    TextField {
        id: startdate
        x: 16
        y: 157
        width: 95
        height: 30
        horizontalAlignment: Text.AlignHCenter
        placeholderText: qsTr("--/--/----")
    }

    TextField {
        id: enddate
        x: 128
        y: 157
        width: 95
        height: 30
        horizontalAlignment: Text.AlignHCenter
        placeholderText: qsTr("--/--/----")
    }

    Text {
        id: _text3
        x: 115
        y: 157
        text: qsTr("-")
        font.pixelSize: 20
    }

    Text {
        id: _text4
        x: 16
        y: 143
        width: 95
        height: 15
        text: qsTr("Date de début :")
        font.pixelSize: 11
    }

    Text {
        id: _text5
        x: 128
        y: 143
        width: 95
        height: 15
        text: qsTr("Date de fin :")
        font.pixelSize: 11
    }

    ListView {
        id: tagslist
        x: 231
        y: 63
        width: 155
        height: 30
        model: tagsListModel
        delegate: Text {
            text: modelData
        }
    }


    ListView {
        id: userslist
        x: 231
        y: 99
        width: 155
        height: 30
        model: usersListModel
        delegate: Text {
            text: modelData
        }
    }


}
