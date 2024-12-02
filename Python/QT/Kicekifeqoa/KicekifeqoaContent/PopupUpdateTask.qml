import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

ApplicationWindow {
    id: popupupdate
    visible: true
    color: "#00ffffff"
    width: 420
    height: 220
    flags: Qt.FramelessWindowHint

    property string taskName: ""            // Propriétés pour pré-remplir les champs
    property int taskPriority: 0
    property string taskTags: ""
    property string taskEndDate: ""
    property bool taskChecked: false

    signal updateTaskName(string taskname)   // Signaux pour envoyer les modifications
    signal updateTaskPriority(int priority)
    signal updateTag(string tagname)
    signal removeLastTag()
    signal updateEndDate(string enddate)
    signal taskCompleted(int status)
    signal validateUpdateInfo()

    Rectangle {
        id: background
        x: 0
        y: 0
        width: 420
        height: 220
        color: Colors.couleur1
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

            Component.onCompleted: {
                if (taskTags && taskTags.length > 0) {
                    const tags = taskTags.split(",");
                    tags.forEach(tag => tagsListModel.append({"tag": tag.trim()}));
                }
            }

            Slider {
                id: priorityslider
                x: 273
                y: 4
                width: 115
                height: 30
                value: taskPriority
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
                onClicked: {
                    updateTag(tagname.text)
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
                anchors.right: close.left
                anchors.top: close.top
                anchors.bottom: parent.bottom
                anchors.rightMargin: 6
                anchors.bottomMargin: 8
                checkable: false
                icon.cache: true
                font.pointSize: 15
                onClicked: {
                    updateTaskName(taskname.text);
                    updateTaskPriority(priorityslider.value);
                    updateEndDate(enddate.text);
                    taskCompleted(checkBox.checked ? 1 : 0);
                    validateUpdateInfo();
                    popupupdate.close();
                }
            }

            Text {
                id: prioritytext
                x: 277
                y: 26
                width: 115
                height: 16
                color: Colors.couleur1
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

            TextField {
                id: taskname
                x: 15
                y: 12
                width: 181
                height: 30
                placeholderText: qsTr("Nom de la tâche")
                text: taskName  // Pré-rempli avec le nom de la tâche
            }

            TextField {
                id: enddate
                x: 15
                y: 157
                width: 95
                height: 30
                horizontalAlignment: Text.AlignHCenter
                placeholderText: qsTr("--/--/----")
                text: taskEndDate  // Pré-rempli avec la date de fin
            }

            Text {
                id: _text5
                x: 15
                y: 143
                width: 95
                height: 15
                color: Colors.couleur1
                text: qsTr("Date de fin :")
                font.pixelSize: 11

                CheckBox {
                    id: checkBox
                    x: 263
                    y: -106
                    width: 150
                    height: 30
                    text: qsTr("Tâche Terminée")
                    scale: 0.8
                    checked: taskChecked  // Pré-rempli avec le statut de la tâche
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
                    popupupdate.close();
                }
            }
        }
    }
}
