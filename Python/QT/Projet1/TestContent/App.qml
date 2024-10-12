import QtQuick
import QtQuick.Controls

Window {
    width: 600
    height: 400
    visible: true
    title: "Test"

    RoundButton {
        id: addcard
        x: 280
        y: 180
        text: "+"
        onClicked: {
            var component = Qt.createComponent("Popup.qml");
            if (component.status === Component.Ready) {
                var popup = component.createObject(parent);
                if (popup === null) {
                    console.error("Erreur lors de la création de Popup");
                } else {

                    popup.addTaskName.connect(taskHandler.add_task_name);
                    popup.addTaskPriority.connect(taskHandler.add_task_priority);
                    popup.addTag.connect(taskHandler.add_tag);
                    popup.removeLastTag.connect(taskHandler.remove_last_tag);
                    popup.addUser.connect(taskHandler.add_user);
                    popup.removeLastUser.connect(taskHandler.remove_last_user);
                    popup.addStartDate.connect(taskHandler.add_start_date);
                    popup.addEndDate.connect(taskHandler.add_end_date);
                    popup.validateInfo.connect(taskHandler.validate_info);
                }
            } else {
                console.error("Erreur lors du chargement de Popup.qml");
            }
        }
    }
}