import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from autogen.settings import url, import_paths
from PySide6.QtCore import qInstallMessageHandler, QtMsgType

from task_handler_Pcreate import TaskHandler as TaskHandlerCreate
from task_handler_Pupdate import TaskHandler as TaskHandlerUpdate

def message_handler(mode, context, message):
    if mode == QtMsgType.QtDebugMsg:
        print(f"Debug: {message}")
    elif mode == QtMsgType.QtInfoMsg:
        print(f"Info: {message}")
    elif mode == QtMsgType.QtWarningMsg:
        print(f"Warning: {message}")
    elif mode == QtMsgType.QtCriticalMsg:
        print(f"Critical: {message}")
    elif mode == QtMsgType.QtFatalMsg:
        print(f"Fatal: {message}")


if __name__ == '__main__':

    qInstallMessageHandler(message_handler)

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent
    engine.addImportPath(os.fspath(app_dir))

    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    task_handler_create = TaskHandlerCreate(engine)
    task_handler_update = TaskHandlerUpdate(engine)

    engine.rootContext().setContextProperty("taskHandlerCreate", task_handler_create)
    engine.rootContext().setContextProperty("taskHandlerUpdate", task_handler_update)

    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
