import os
import sys
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from autogen.settings import url, import_paths
from task_handler_Pcreate import TaskHandler

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    app_dir = Path(__file__).parent.parent
    engine.addImportPath(os.fspath(app_dir))

    for path in import_paths:
        engine.addImportPath(os.fspath(app_dir / path))

    task_handler = TaskHandler(engine)
    engine.rootContext().setContextProperty("taskHandler", task_handler)

    engine.load(os.fspath(app_dir / url))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
