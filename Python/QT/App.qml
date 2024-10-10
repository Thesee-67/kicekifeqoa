import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Task Manager"

    signal taskName(string name)
    signal taskPriority(int priority)
    signal addTag(string tag)
    signal removeTag(string tag)
    signal addUser(string email)
    signal removeUser(string email)

    Column {
        anchors.centerIn: parent
        spacing: 20

        // Row for Task Name
        Row {
            spacing: 10
            TextField {
                id: taskNameField
                placeholderText: "Enter Task Name"
                width: 200
            }
            Button {
                text: "Submit Task Name"
                onClicked: {
                    taskName(taskNameField.text)
                }
            }
        }

        // Row for Task Priority
        Row {
            spacing: 10
            Slider {
                id: prioritySlider
                from: 0
                to: 100
                stepSize: 1
                width: 200
            }
            Button {
                text: "Submit Task Priority"
                onClicked: {
                    taskPriority(prioritySlider.value)
                }
            }
        }

        // Row for adding and removing tags
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
                }
            }
            Button {
                text: "Remove Tag"
                onClicked: {
                    removeTag(tagField.text)
                }
            }
        }

        // Row for adding and removing users
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
                }
            }
            Button {
                text: "Remove User"
                onClicked: {
                    removeUser(userEmailField.text)
                }
            }
        }
    }
}
