import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 600
    height: 400
    title: "Task Manager"

    signal updateTaskName(string name)
    signal updateTaskPriority(int priority)
    signal addTag(string tag)
    signal removeLastTag()
    signal addUser(string email)
    signal removeLastUser()
    signal printAllInfo()

    property var tagsListModel: []
    property var usersListModel: []

    Column {
        anchors.centerIn: parent
        spacing: 20

        // Task Name Field with default text "Tache 1"
        TextField {
            id: taskNameField
            width: 176
            height: 20
            text: "Tache 1"  // Default text value
            placeholderText: "Enter Task Name"
        }

        // Task Priority Slider
        Row {
            spacing: 10
            Slider {
                id: prioritySlider
                from: 0
                to: 2
                stepSize: 1
                width: 200
            }

            // Display priority level as text
            Text {
                text: prioritySlider.value === 0 ? "Priorité basse"
                     : prioritySlider.value === 1 ? "Priorité moyenne"
                     : "URGENT"
            }
        }

        // Row for adding/removing tags
        Row {
            spacing: 10
            TextField {
                id: tagField
                placeholderText: "Enter Tag"
                width: 200
            }
            Button {
                text: "Add Tag"
                onClicked: {
                    addTag(tagField.text)
                    tagField.text = ""
                }
            }
            Button {
                text: "Remove Last Tag"
                onClicked: {
                    removeLastTag()
                }
            }
        }

        // Display list of tags horizontally
        Row {
            width: parent.width
            spacing: 10
            Repeater {
                model: tagsListModel
                delegate: Text {
                    text: modelData
                    padding: 5
                }
            }
        }

        // Row for adding/removing users
        Row {
            spacing: 10
            TextField {
                id: userEmailField
                placeholderText: "Enter User Email"
                width: 200
            }
            Button {
                text: "Add User"
                onClicked: {
                    addUser(userEmailField.text)
                    userEmailField.text = ""
                }
            }
            Button {
                text: "Remove Last User"
                onClicked: {
                    removeLastUser()
                }
            }
        }

        // Display list of users vertically
        ListView {
            width: 200
            height: 100
            model: usersListModel
            delegate: Text {
                text: modelData
            }
        }

        // Final button to print all information
        Button {
            text: "Print All Information"
            onClicked: {
                // Update the task name and priority when this button is pressed
                updateTaskName(taskNameField.text)
                updateTaskPriority(prioritySlider.value)
                printAllInfo()
            }
        }
    }
}
