import os
import sys
import signal
from src.AplicationWindow import AplicationWindow
from PyQt6.QtCore import QFileSystemWatcher
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)
files = [os.path.expanduser('~') + '/.config/vasak/vasak.conf']
watcher = QFileSystemWatcher(files)
watcher.addPaths(files)

if __name__ == "__main__":
    app.setApplicationName("Application Template")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationName("Vasak Group")
    window = AplicationWindow(app)
    window.show()
    watcher.fileChanged.connect(window.load_ui_config)
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Habilitar Ctrl+C
    sys.exit(app.exec())
