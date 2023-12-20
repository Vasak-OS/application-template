from Vasak.VSKWindow import VSKWindow
from src.AplicationBinding import AplicationBinding
from PyQt6.QtWidgets import QApplication

class AplicationWindow(VSKWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.shareObject = AplicationBinding(self, app)
        self.channel.registerObject("vsk", self.shareObject)
        self.load_html("ui/dist/index.html") # Cargar un HTML en el WebView
