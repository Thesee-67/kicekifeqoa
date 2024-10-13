import QtQuick 2.15
import QtQuick.Controls 2.15

Window {
    visible: true
    width: 400
    height: 200
    title: "Nouvelle Tâche"

    signal addTaskName(string taskname)
    signal addTaskPriority(int priority)
    signal addTag(string username)
    signal removeLastTag()
    signal addUser(string user)
    signal removeLastUser()
    signal addStartDate(string startdate)
    signal addEndDate(string enddate)
    signal taskCompleted(int status)
    signal validateInfo()


    ListModel {
        id: tagsListModel
    }

    ListModel {
        id: usersListModel
    }

    Slider {
        id: priorityslider
        x: 277
        y: 8
        width: 115
        height: 30
        value: 0
        scale: 0.7
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
            tagsListModel.append({"tag": tagname.text});
            tagname.text = "";
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
            if (tagsListModel.count > 0) {
                tagsListModel.remove(tagsListModel.count - 1)
                removeLastTag();
            }
        }
    }

    RoundButton {
        id: validate
        x: 352
        y: 152
        text: "\u2713"
        font.pointSize: 15
        onClicked: {
            addTaskName(taskname.text);
            addTaskPriority(priorityslider.value);
            addStartDate(startdate.text)
            addEndDate(enddate.text)
            taskCompleted(checkBox.checked ? 1 : 0);
            validateInfo();
        }
    }

    Text {
        id: prioritytext
        x: 277
        y: 31
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
            usersListModel.append({"user": username.text});
            username.text = "";
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
            if (usersListModel.count > 0) {
                usersListModel.remove(usersListModel.count - 1)
                removeLastUser();
            }
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

        CheckBox {
            id: checkBox
            x: 97
            y: 13
            width: 150
            height: 30
            text: qsTr("Tache Terminée")
            scale: 0.8
            checkState: Qt.Unchecked
        }
    }


    Flickable {
        id: tagsFlickable
        x: 231
        y: 68
        width: 150
        height: 30
        contentWidth: tagsRow.width
        contentHeight: tagsRow.height
        clip: true

        Row {
            id: tagsRow
            spacing: 10
            Repeater {
                model: tagsListModel
                delegate: Text {
                    text: model.tag
                }
            }
        }
    }


    Flickable {
        id: usersFlickable
        x: 231
        y: 104
        width: 150
        height: 30
        contentWidth: usersRow.width
        contentHeight: usersRow.height
        clip: true

        Row {
            id: usersRow
            spacing: 10
            Repeater {
                model: usersListModel
                delegate: Text {
                    text: model.user
                }
            }
        }
    }

    MouseArea {
        id: mouseArea
        x: 231
        y: 63
        width: 150
        height: 66
        enabled: false
        cursorShape: Qt.DragMoveCursor
    }
}