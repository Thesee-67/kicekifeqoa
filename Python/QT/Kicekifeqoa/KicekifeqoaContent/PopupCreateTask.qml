import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: popupcreate
    visible: true
    color: "#00ffffff"
    width: 420
    height: 220
    flags: Qt.FramelessWindowHint

    signal addTaskName(string taskname)
    signal addTaskPriority(int priority)
    signal addTag(string tagname)
    signal removeLastTag()
    signal addUser(string username)
    signal removeLastUser()
    signal addEndDate(string enddate)
    signal taskCompleted(int status)
    signal validateInfo()

    Rectangle {
        id: background
        x: 0
        y: 0
        width: 420
        height: 220
        color: "#4e598c"
        radius: 10
        border.width: 0

        Rectangle {
        id: rectangle
        x: 10
        y: 10
        width: 400
        height: 200
        visible: true
        radius: 10
        anchors.verticalCenter: parent.verticalCenter
        anchors.verticalCenterOffset: 0
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        ListModel {
        id: tagsListModel
    }

    ListModel {
        id: usersListModel
    }

    Slider {
        id: priorityslider
        x: 273
        y: 4
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
        x: 173
        y: 65
        width: 20
        height: 20
        text: "+"
        highlighted: false
        flat: false
        icon.color: "#4e598c"
        onClicked: {
            addTag(tagname.text)
            tagsListModel.append({"tag": tagname.text});
            tagname.text = "";
        }
    }

    RoundButton {
        id: tagremove
        x: 199
        y: 65
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
        x: 306
        y: 152
        text: "\u2713"
        anchors.verticalCenter: close.verticalCenter
        anchors.right: close.left
        anchors.top: close.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 6
        anchors.bottomMargin: 8
        checkable: false
        icon.cache: true
        font.pointSize: 15
        onClicked: {
            addTaskName(taskname.text);
            addTaskPriority(priorityslider.value);
            addEndDate(enddate.text);
            taskCompleted(checkBox.checked ? 1 : 0);
            validateInfo();
            popupcreate.close();
        }
    }

    Text {
        id: prioritytext
        x: 277
        y: 26
        width: 115
        height: 16
        color: "#4e598c"
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
        text: priorityslider.value === 0 ? "Priorité basse"
             : priorityslider.value === 1 ? "Priorité moyenne"
                                          : "URGENT"
        anchors.right: parent.right
             anchors.rightMargin: 8
    }

    TextField {
        id: tagname
        x: 15
        y: 63
        width: 155
        height: 30
        placeholderText: qsTr("Etiquettes")
    }

    RoundButton {
        id: useradd
        x: 173
        y: 107
        width: 20
        height: 20
        text: "+"
        anchors.right: tagadd.right
        onClicked: {
            addUser(username.text)
            usersListModel.append({"user": username.text});
            username.text = "";
        }
    }

    RoundButton {
        id: userremove
        x: 199
        y: 107
        width: 20
        height: 20
        text: "-"
        anchors.right: tagremove.right
        onClicked: {
            if (usersListModel.count > 0) {
                usersListModel.remove(usersListModel.count - 1)
                removeLastUser();
            }
        }
    }

    TextField {
        id: taskname
        x: 15
        y: 12
        width: 181
        height: 30
        placeholderText: qsTr("Nom de la tâche")
    }

    TextField {
        id: enddate
        x: 15
        y: 157
        width: 95
        height: 30
        horizontalAlignment: Text.AlignHCenter
        placeholderText: qsTr("--/--/----")
    }

    Text {
        id: _text5
        x: 15
        y: 143
        width: 95
        height: 15
        color: "#4e598c"
        text: qsTr("Date de fin :")
        font.pixelSize: 11

        CheckBox {
            id: checkBox
            x: 263
            y: -106
            width: 150
            height: 30
            text: qsTr("Tache Terminée")
            scale: 0.8
            checkState: Qt.Unchecked
        }
    }


    Flickable {
        id: tagsFlickable
        x: 227
        y: 65
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
        x: 227
        y: 102
        width: 150
        height: 30
        anchors.right: prioritytext.right
        anchors.rightMargin: 15
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
        x: 225
        y: 65
        width: 150
        height: 66
        anchors.right: tagsFlickable.right
        enabled: false
        cursorShape: Qt.DragMoveCursor

        ComboBox {
            id: username
            x: -212
            y: 39
            width: 155
            height: 29
        }
    }

    RoundButton {
        id: close
        x: 352
        y: 152
        text: "X"
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 8
        anchors.topMargin: 6
        anchors.bottomMargin: 8
        font.pointSize: 15
        onClicked: {
            popupcreate.close();
        }
    }
    }
}
}