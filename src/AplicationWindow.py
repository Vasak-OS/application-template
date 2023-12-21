from Vasak.VSKWindow import VSKWindow
from src.AplicationBinding import AplicationBinding
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt

class AplicationWindow(VSKWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.shareObject = AplicationBinding(self, app)
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView

    def set_position(self):
        self.setWindowFlags(
            self.windowFlags() | Qt.WindowType.FramelessWindowHint 
        )