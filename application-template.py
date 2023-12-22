import sys
import signal
from src.AplicationWindow import AplicationWindow
from PyQt6.QtWidgets import QApplication


app = QApplication(sys.argv)

if __name__ == "__main__":
    app.setApplicationName("Application Template")
    app.setApplicationVersion("0.0.1")
    app.setOrganizationName("Vasak Group")
    window = AplicationWindow(app)
    window.show()
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # Habilitar Ctrl+C
    sys.exit(app.exec())
